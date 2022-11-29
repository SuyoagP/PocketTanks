from Game.Tank import Tank
from Game.Weapon import Weapon

class Player:

    def __init__(self, tank, turn=False, weapon=None):
        self.tank = tank
        self.turn = turn
        self.weapon = weapon
        self.lockedTurn = False

    def getWeapon(self) -> Weapon:
        return self.weapon
    def setWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def getTurn(self) -> bool:
        return self.turn
    def setTurn(self, turn: bool):
        self.turn = turn

    def getTank(self) -> Tank:
        return self.tank
    def setTank(self, tank: Tank):
        self.tank = tank

    def getLockedTurn(self) -> bool:
        return self.lockedTurn
    def setLockedTurn(self, lockedTurn:bool):
        self.lockedTurn = lockedTurn

