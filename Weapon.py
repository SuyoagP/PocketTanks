class Weapon:
    #Found at https://stackoverflow.com/questions/2094658/how-do-i-declare-an-attribute-in-python-without-a-value
    damage = None
    terrainDestroy = None

class Bullet(Weapon):
    damage = 10
    terrainDestroy = False

class MagicWall(Weapon):
    damage = 0
    terrainDestroy = False

class MountainMover(Weapon):
    damage = 0
    terrainDestroy = True



