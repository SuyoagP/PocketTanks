import random
from Dependencies.cmu_112_graphics import *
from Game.Move import *
from Weapon import *


class Graphics:
    #https://www.geeksforgeeks.org/class-method-vs-static-method-python/ found here
    def __init__(self, app, canvas):
        self.canvas = canvas
        self.app = app
        self.tankOneY = app.height
        self.tankTwoY = app.height


    def createBackground(self):
        self.canvas.create_image(200, 200, image=ImageTk.PhotoImage(self.app.image2))

    def updateTerrain(self):
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
                                text=f'Player {playerText} Health \n {player}',
                                font='Arial 16 bold', fill='black')

    def createPlayerPowerAngle(self, player1, player2):
        if player1.turn == True:
            self.canvas.create_text(self.app.width / 2 - self.app.width / 4, (self.app.width / 4) * 3,
                                    text=f'Power : {player1.getWeapon().power}', font='Arial 16 bold', fill='black')
            self.canvas.create_text(self.app.width / 2 + self.app.width / 4, (self.app.width / 4) * 3, text=f'Angle {player1.getWeapon().angle}',
                                    font='Arial 16 bold', fill='black')

        elif player2.turn == True:
            self.canvas.create_text(self.app.width / 2 - self.app.width / 4, (self.app.width / 4) * 3,
                                    text=f'Power : {player2.getWeapon().power}', font='Arial 16 bold', fill='black')
            self.canvas.create_text(self.app.width / 2 + self.app.width / 4, (self.app.width / 4) * 3, text=f'Angle {player2.getWeapon().angle}',
                                    font='Arial 16 bold', fill='black')

    @staticmethod
    def createTerrain(app):
        from Params import player1,player2
        startPoint, startHeight = 0, app.height
        endPoint, endHeight = app.width + 25, int(app.height * (random.randint(0, 6) / 10))

        left, right = startPoint, startPoint + 25
        for newRight in range(right, endPoint, 25):

            top, bottom = app.height - 25, app.height
            randHeight = endHeight + int(app.height * (random.randint(0, 3) / 10))
            if newRight == 75:
                player1.getTank().y0 = randHeight + 15
                player1.getTank().y1 = randHeight + 25
                player1.getWeapon().currY = randHeight + 15
            elif newRight == 225:
                player2.getTank().y0 = randHeight + 15
                player2.getTank().y1 = randHeight + 25
                player2.getWeapon().currY = randHeight + 15
            for newTop in range(app.height, randHeight, -25):
                bottom, top = top, newTop
                app.rectangleCoords.append((left, top, right, bottom))
            left, right = right, newRight + 25
