from ursina import *
from ursina import vec3


class Test_cube(Entity):
    def __init__(self,):
        super().__init__(model="cube", color=color.white,
                         texture="white_cube", rotation=Vec3(45, 45, 45))


def update():
    if held_keys["a"]:
        test_square.x -= 1 * time.dt


class Test_Button(Button):
    def __init__(self):
        super().__init__(parent=scene, model="cube", texture="brick",
                         color=color.blue, pressed_color=color.lime, highlight_color=color.red)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                print("Button presssed")


app = Ursina()
test_square = Entity(model="quad", color=color.blue,
                     scale=(1, 4), position=(5, 1))
# sans = Entity(model="quad", texture="assets\\220px-Sans_undertale.jpg")

# test_cube = Test_cube()
button = Test_Button()
app.run()
