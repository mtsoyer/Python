from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# class Voxel(Button):
#     def __init__(self, position=(0, 0, 0)):
#         super().__init__(
#             parent=scene,
#             postiion=position,
#             model="cube",
#             origin_y=0.5,
#             texture="white_cube",
#             color=color.white,
#             highlight_color=color.lime)


app = Ursina()


def update():
    pass


terrainWidth = 10
for i in range(terrainWidth * terrainWidth):
    bud = Entity(model=" cube", color=color.green, texture="white_cube")
    bud.x = i/terrainWidth
    bud.y = 0
    bud.z = i/terrainWidth


subject = FirstPersonController()
subject.y = 12
subject.x = subject.z = 5

# for z in range(8):
#     for x in range(8):
#         voxel = Voxel(position= (x, 0, z))

# voxel = Voxel(position= ())
        
# player = FirstPersonController()

app.run()
