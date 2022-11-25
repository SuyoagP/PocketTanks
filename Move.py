from Tank import Tank
from Weapon import Weapon, Bullet, MagicWall, MountainMover
class Move:
    def __init__(self, shooter:Tank, victim:Tank, weaponType:Weapon, angle = 45, power = 50, fire = False):
        self.weaponType = weaponType
        self.shooter = shooter
        self.victim = victim
        self.angle = angle
        self.power = power
        self.fire = fire
    def changeAngle(self, dTheta):
        self.angle += dTheta
    def changePower(self, dPower):
        self.power += dPower
    # def executeMove(self):
    #     x0,y0 = newBullet.currX, newBullet.currY
    #     if (x0 > (playerTwo.x0) and x0 < playerTwo.x1 and (y0 > playerTwo.y0) and y0 < playerTwo.y1):
    #         self.victim.damage(self.weaponType)







