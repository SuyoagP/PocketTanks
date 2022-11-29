import math
from Dependencies.cmu_112_graphics import *


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
        self.outOfBounds = False
        self.hit = False
        self.time = 0
    def weaponFireOne(self, angle, power, time, x0, y0, app, victimx0, victimy0, victimx1, victimy1):

        gravity = 9.81
        vx = 100 * power * math.cos(math.radians(angle))
        vy = 100 * power * math.sin(math.radians(angle))
        self.currX = x0 + vx * self.time
        self.currY = y0 - (vy * self.time - 0.5 * gravity * self.time ** 2)
        #Out of bounds check
        if self.currX > app.width or self.currX < 0 or self.currY > app.height:
            self.currX = x0
            self.currY = y0
            self.outOfBounds = True
            return
        #Check if it has hit opponent
        if (self.currX > victimx0 and self.currX < victimx1) and (self.currY > victimy0 and self.currY < victimy1):
            print("OH YEAH")
            self.hit = True
            self.currX = x0
            self.currY = y0
            return
        self.time += 0.002
    def weaponFireTwo(self, angle, power, time, x0, y0, app, victimx0, victimy0, victimx1, victimy1):

        gravity = 9.81
        vx = 100 * power * math.cos(math.radians(angle))
        vy = 100 * power * math.sin(math.radians(angle))
        self.currX = x0 - vx * self.time
        self.currY = y0 - (vy * self.time - 0.5 * gravity * self.time ** 2)
        #Out of bounds check
        if self.currX > app.width or self.currX < 0 or self.currY > app.height:
            self.currX = x0
            self.currY = y0
            self.outOfBounds = True
            return

        #Check if it has hit opponent
        if (self.currX > victimx0 and self.currX < victimx1) and (self.currY > victimy0 and self.currY < victimy1):
            print("OH YEAH")
            self.hit = True
            self.currX = x0
            self.currY = y0
            return
        self.time += 0.002


    def destroyTerrain(self, app):
        print(self.terrainDestroy)
        if self.terrainDestroy == True:
            for block in app.rectangleCoords:
                print(block)
                x0, y0, x1, y1 = block
                if (self.currX > min(x0, x1) and self.currX < max(x0, x1)) and (self.currY > min(y0, y1) and self.currY < max(y0, y1)):
                    app.rectangleCoords.remove(block)


class Bullet(Weapon):
    damage = 10
    terrainDestroy = False

class MagicWall(Weapon):
    damage = 0
    terrainDestroy = False

class MountainMover(Weapon):
    damage = 0
    terrainDestroy = True



