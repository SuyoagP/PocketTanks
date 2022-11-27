from Dependencies.cmu_112_graphics import *
from Game.Move import *
from Weapon import *

class Graphics:
    #https://www.geeksforgeeks.org/class-method-vs-static-method-python/ found here
    def __init__(self, app, canvas):
        self.canvas = canvas
        self.app = app

    def createBackground(self):
        self.app.image2 = self.app.scaleImage(self.app.image1, 2 / 3)
        self.canvas.create_image(200, 200, image=ImageTk.PhotoImage(self.app.image2))

    def createTerrain(self):
        for coords in self.app.rectangleCoords:
            x1, y1, x2, y2 = coords
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='green')

    def createBulletRight(self, bullet: Bullet, color: StringVar):
        self.canvas.create_oval(bullet.currX, bullet.currY, bullet.currX + 5, bullet.currY + 2,
                           fill=color)

    def createBulletLeft(self, bullet: Bullet, color: StringVar):
        self.canvas.create_oval(bullet.currX, bullet.currY, bullet.currX - 5, bullet.currY + 2,
                                fill=color)

    def createTank(self, player):
        self.canvas.create_rectangle(player.x0, player.y0, player.x1, player.y1,
                                     fill=player.color)

    def createPlayerHealth(self, displacement, player, playerText):
        self.canvas.create_text(self.app.width / 10 + displacement, self.app.width / 8,
                                text=f'Player {playerText} Health \n {player.health}',
                                font='Arial 16 bold', fill='black')

    def createPlayerPowerAngle(self, playerOneMove: Move, playerTwoMove: Move):
        if playerOneMove.Move == True:
            self.canvas.create_text(self.app.width / 2 - self.app.width / 4, (self.app.width / 4) * 3,
                                    text=f'Power : {playerOneMove.power}', font='Arial 16 bold', fill='black')
            self.canvas.create_text(self.app.width / 2 + self.app.width / 4, (self.app.width / 4) * 3, text=f'Angle {playerOneMove.angle}',
                                    font='Arial 16 bold', fill='black')

        elif playerTwoMove.Move == True:
            self.canvas.create_text(self.app.width / 2 - self.app.width / 4, (self.app.width / 4) * 3,
                                    text=f'Power : {playerTwoMove.power}', font='Arial 16 bold', fill='black')
            self.canvas.create_text(self.app.width / 2 + self.app.width / 4, (self.app.width / 4) * 3, text=f'Angle {playerTwoMove.angle}',
                                    font='Arial 16 bold', fill='black')
