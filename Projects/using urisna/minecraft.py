from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture("video/assets/grass_block.png")
stone_texture = load_texture("video/assets/stone_block.png")
brick_texture = load_texture("video/assets/brick_block.png")
dirt_texture = load_texture("video/assets/dirt_block.png")
sky_texture = load_texture("video/assets/skybox.png")
arm_texture = load_texture("video/assets/arm_texture.png")
blocksound = Audio('video/assets/punch_sound.wav', autoplay= False, loop = False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
    global block_pick
    if held_keys["1"] : block_pick = 1
    if held_keys["2"] : block_pick = 2
    if held_keys["3"] : block_pick = 3
    if held_keys["4"] : block_pick = 4
    if held_keys["left mouse"] or held_keys["right mouse"]: arm.active() 
    else: arm.passive()
                                            

class Voxel(Button):
    def __init__(self, pos=(0, 0, 0), texture = grass_texture):
        super().__init__(
            parent=scene,
            position=pos,
            model="assets/block",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            # highlight_color=color.lime,
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                blocksound.play()
                if block_pick == 1 : voxel = Voxel(pos=self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2 : voxel = Voxel(pos=self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3 : voxel = Voxel(pos=self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4 : voxel = Voxel(pos=self.position + mouse.normal, texture = dirt_texture)
                
            if key == "right mouse down":
                blocksound.play()
                destroy(self)
    
          


class sky(Entity):
    def __init__(self):
        super().__init__(parent = scene,
                         model = "sphere",
                         texture = sky_texture,
                         scale = 150,
                         double_sided = True,)

class arm(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui,
                         model ="assets/arm",
                         texture = arm_texture,
                         scale = 0.2,
                         position = Vec2(0.4, -0.6),
                         rotation = Vec3(150, -10, 0))
    def active(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)

def input(key):
    if key == "q" or key == "escape":
        quit()


for z in range(20):
    for x in range(20):
        voxel = Voxel(pos=(x, 0, z))
player = FirstPersonController()
sky = sky()
arm = arm()


app.run()
