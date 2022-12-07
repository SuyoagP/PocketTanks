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
        self.tankHit = False
        self.terrainHit = False
        self.time = 0
    def weaponFireOne(self, angle, power, time, x0, y0, app, victimx0, victimy0, victimx1, victimy1):

        gravity = 9.81
        vx = 2*power * math.cos(math.radians(angle))
        vy = 2*power * math.sin(math.radians(angle))
        self.currX = x0 + vx * self.time
        self.currY = y0 - (vy * self.time - 0.5 * gravity * self.time ** 2)
        #Out of bounds check
        if self.currX > app.width or self.currX < 0 or self.currY > app.height:
            self.currX = x0
            self.currY = y0
            self.outOfBounds = True
            return

        #terrain hit check
        for block in app.rectangleCoords:
            blockX0, blockY0, blockX1, blockY1 = block
            if (self.currX >= min(blockX0, blockX1) and self.currX <= max(blockX0, blockX1)) and (
                    self.currY >= min(blockY0, blockY1) and self.currY <= max(blockY0, blockY1)):
                self.terrainHit = True
                if self.terrainDestroy == True:
                    app.rectangleCoords.remove(block)
                elif self.terrainCreate == True:
                    app.rectangleCoords.append((blockX0, blockY0 - 25, blockX1, blockY1 - 50))
                    app.rectangleCoords.append((blockX0, blockY0 - 50, blockX1, blockY1 - 75))
                    app.rectangleCoords.append((blockX0, blockY0 - 75, blockX1, blockY1 - 100))

                self.currX = x0
                self.currY = y0
                return

        #Check if it has hit opponent
        if (self.currX > victimx0 and self.currX < victimx1) and (self.currY > victimy0 and self.currY < victimy1):
            print("OH YEAH")
            self.tankHit = True
            self.currX = x0
            self.currY = y0
            return
        self.time += 0.02

    def weaponFireTwo(self, angle, power, time, x0, y0, app, victimx0, victimy0, victimx1, victimy1):

        gravity = 9.81
        vx = 2*power * math.cos(math.radians(angle))
        vy = 2*power * math.sin(math.radians(angle))
        self.currX = x0 - vx * self.time
        self.currY = y0 - (vy * self.time - 0.5 * gravity * self.time ** 2)
        # Out of bounds check
        if self.currX > app.width or self.currX < 0 or self.currY > app.height:
            self.currX = x0
            self.currY = y0
            self.outOfBounds = True
            return

        # terrain hit check
        for block in app.rectangleCoords:
            blockX0, blockY0, blockX1, blockY1 = block
            if (self.currX >= min(blockX0, blockX1) and self.currX <= max(blockX0, blockX1)) and (self.currY >= min(blockY0, blockY1) and self.currY <= max(blockY0, blockY1)):
                self.terrainHit = True
                if self.terrainDestroy == True:
                    app.rectangleCoords.remove(block)
                elif self.terrainCreate == True:
                    app.rectangleCoords.append((blockX0, blockY0 - 25, blockX1, blockY1 - 50))
                    app.rectangleCoords.append((blockX0, blockY0 - 50, blockX1, blockY1 - 75))
                    app.rectangleCoords.append((blockX0, blockY0 - 75, blockX1, blockY1 - 100))

                self.currX = x0
                self.currY = y0
                return

        # Check if it has hit opponent
        if (self.currX > victimx0 and self.currX < victimx1) and (self.currY > victimy0 and self.currY < victimy1):
            print("OH YEAH")
            self.tankHit = True
            self.currX = x0
            self.currY = y0
            return
        self.time += 0.2


    def destroyTerrain(self, app):
        for block in app.rectangleCoords:
            x0, y0, x1, y1 = block
            if (self.currX > min(x0, x1) and self.currX < max(x0, x1)) and (self.currY > min(y0, y1) and self.currY < max(y0, y1)):
                app.rectangleCoords.remove(block)


class Bullet(Weapon):
    damage = 10
    terrainDestroy = False
    terrainCreate = False

class MagicWall(Weapon):
    damage = 0
    terrainDestroy = False
    terrainCreate = True

class MountainMover(Weapon):
    damage = 0
    terrainDestroy = True
    terrainCreate = False



