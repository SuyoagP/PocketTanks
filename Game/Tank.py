from Weapon import Weapon
class Tank(object):

    def __init__(self, color, health, player, x0, y0, x1, y1):
        self.color = color
        self.health = health
        self.player = player
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    #Found at https://stackoverflow.com/questions/51164723/python-3-type-hints-for-function-signature
    def damage(self, weaponType: Weapon):
        self.health -= weaponType.damage

    def move(self, x0Offset, x1Offset, y0Offset, y1Offset):
        self.x0 += x0Offset
        self.x1 += x1Offset
        self.y0 += y0Offset
        self.y1 += y1Offset



    def getHealth(self):
        return self.health

    def getPlayer(self):
        return self.player

    def getColor(self):
        return self.color

    def getx0(self):
        return self.x0

    def gety0(self):
        return self.y0

    def getx1(self):
        return self.x1

    def gety1(self):
        return self.y1