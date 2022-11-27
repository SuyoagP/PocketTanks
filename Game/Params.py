from Game.Move import Move
from Game.Tank import Tank
from Game.Weapon import Bullet

playerOne = Tank('red', 100, True, 50, 390, 75, 400)
playerTwo = Tank('purple', 100, True, 285, 390, 310, 400)
newBullet = Bullet(playerOne.getx1(), playerOne.gety0(), 45, 50, False, 76, 390)
newBulletTwo = Bullet(playerTwo.getx0(), playerTwo.gety0(), 45, 50, False, 285, 390)
playerOneMove = Move(playerOne, playerTwo, newBullet, True, 45, 50, False)
playerTwoMove = Move(playerTwo, playerOne, newBulletTwo, False, 45, 50, False)
