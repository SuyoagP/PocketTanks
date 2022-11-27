from Tank import Tank
from Weapon import Weapon, Bullet, MagicWall, MountainMover


class Move:
    def __init__(self, shooter:Tank, victim:Tank, weaponType:Weapon,Move, angle = 45, power = 50, fire = False):
        self.weaponType = weaponType
        self.shooter = shooter
        self.victim = victim
        self.angle = angle
        self.power = power
        self.fire = fire
        self.Move = Move
    def changeAngle(self, dTheta):
        self.angle += dTheta
    def changePower(self, dPower):
        self.power += dPower
    def executeMove(self,other):
        x0,y0 = self.weaponType.currX, self.weaponType.currY
        if self.Move == True:
            if (x0 > (self.victim.x0) and x0 < self.victim.x1 and (y0 > self.victim.y0) and y0 < self.victim.y1):
                self.victim.damage(self.weaponType)
                self.Move = False
                other.Move = True









