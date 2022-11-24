import math
from cmu_112_graphics import *

class Weapon(App):
    #Found at https://stackoverflow.com/questions/2094658/how-do-i-declare-an-attribute-in-python-without-a-value
    damage = None
    terrainDestroy = None
    def __init__(self, currX, currY):
        self.currX = currX
        self.currY = currY
    def weaponLocation(self, angle, power, time):
        self.currX = time
        self.currY = (-power/math.atan(angle))*(time - power)



class Bullet(Weapon):
    damage = 10
    terrainDestroy = False

class MagicWall(Weapon):
    damage = 0
    terrainDestroy = False

class MountainMover(Weapon):
    damage = 0
    terrainDestroy = True



