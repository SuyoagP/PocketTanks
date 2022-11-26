import math
from cmu_112_graphics import *



class Weapon(App):
    #Found at https://stackoverflow.com/questions/2094658/how-do-i-declare-an-attribute-in-python-without-a-value
    damage = None
    terrainDestroy = None
    def __init__(self, currX, currY,angle,power,fired,startX,startY):
        self.startX = startX
        self.startY = startY
        self.currX = currX
        self.currY = currY
        self.angle = angle
        self.power = power
        self.fire = fired
    def weaponLocation(self, angle, power, time, x0, y0,app):
        if self.fire == True:
            gravity = 9.81
            vx = 2 * power * math.cos(math.radians(angle))
            vy = 2 * power * math.sin(math.radians(angle))
            self.currX = x0 + vx * time
            self.currY = y0 - (vy * time - 0.5 * gravity * time ** 2)
        if self.currX > app.width or self.currX < 0 or self.currY > app.height:
            self.currX = x0
            self.currY = y0





class Bullet(Weapon):
    damage = 10
    terrainDestroy = False

class MagicWall(Weapon):
    damage = 0
    terrainDestroy = False

class MountainMover(Weapon):
    damage = 0
    terrainDestroy = True



