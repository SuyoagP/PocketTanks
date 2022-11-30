from Game.Player import Player
from Game.Tank import Tank
from Graphics import *
from Game.Weapon import Bullet


p1Tank = Tank('red', 20, True, 50, 190, 75, 200)
p2Tank = Tank('purple', 20, True, 200, 390, 225, 400)

player1 = Player(
    tank=p1Tank,
    turn=True,
    weapon=Bullet(p1Tank.getx1(), p1Tank.gety0(), 45, 50, False, 76, 390)
)
player2 = Player(
    tank=p2Tank,
    turn=False,
    weapon=Bullet(p2Tank.getx0(), p2Tank.gety0(), 45, 50, False, 285, 390)
)

