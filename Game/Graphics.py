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
        #https://www.stockvault.net/photo/279149/black-and-purple-gradient-background Image found here
        self.canvas.create_image(self.app.width/2, self.app.height/2 + 20, image=ImageTk.PhotoImage(self.app.image2))

    def updateTerrain(self):
        for coords in self.app.rectangleCoords:
            x1, y1, x2, y2 = coords
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='green')

    def createBulletRight(self, bullet: Bullet, color: StringVar):
        self.canvas.create_oval(bullet.currX, bullet.currY, bullet.currX + 5, bullet.currY + 4,
                           fill=color)

    def createBulletLeft(self, bullet: Bullet, color: StringVar):
        self.canvas.create_oval(bullet.currX, bullet.currY, bullet.currX - 5, bullet.currY + 4,
                                fill=color)

    def createTankTwo(self, player):
        self.canvas.create_image(player.x0+10, player.y0, image=ImageTk.PhotoImage(self.app.tankImageTwo))

    def createTankOne(self, player):
        self.canvas.create_image(player.x0 + 10, player.y0, image=ImageTk.PhotoImage(self.app.tankImageOne))


    def createPlayerHealth(self, displacement, player, playerText):
        self.canvas.create_text(self.app.width / 8 + displacement, self.app.width / 8,
                                text=f'Player {playerText} Health \n {player}',
                                font='Futura 20', fill='White')

    def createPlayerPowerAngle(self, player1, player2):
        self.canvas.create_rectangle(self.app.width/2-self.app.width/6,0, self.app.width/2+self.app.width/6,self.app.height*0.2,fill = 'grey')
        self.canvas.create_text(self.app.width / 2 , self.app.height / 15,
                                text='Mission Control', font='Futura 22', fill='black')
        if player1.turn == True:
            self.canvas.create_text(self.app.width/2-self.app.width/10, self.app.height /10,text=f'Power : {player1.getWeapon().power}', font='Futura 16', fill='black')
            self.canvas.create_text(self.app.width/2+self.app.width/10, self.app.height /10, text=f'Angle : {player1.getWeapon().angle}',
                                    font='Futura 16', fill='black')

        elif player2.turn == True:
            self.canvas.create_text(self.app.width/2-self.app.width/10, self.app.height /10,text=f'Power : {player2.getWeapon().power}', font='Futura 16', fill='black')
            self.canvas.create_text(self.app.width/2+self.app.width/10, self.app.height /10, text=f'Angle : {player2.getWeapon().angle}',
                                    font='Futura 16', fill='black')

    @staticmethod
    #https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjCwvWajdb7AhXxmokEHd9UDv0QFnoECAwQAQ&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fclass-method-vs-static-method-python%2F&usg=AOvVaw0q2GoARgy4NFTwE86n5kW5
    def createTerrain(app):
        from Params import player1,player2
        startPoint, startHeight = 0, app.height
        endPoint, endHeight = app.width + 25, int(app.height * (random.randint(4, 6) / 10))

        left, right = startPoint, startPoint + 25
        for newRight in range(right, endPoint, 25):

            top, bottom = app.height - 25, app.height
            randHeight = endHeight + int(app.height * (random.randint(0, 3) / 10))
            if newRight == 75:
                player1.getTank().y0 = randHeight + 15
                player1.getTank().y1 = randHeight + 25
                player1.getWeapon().currY = randHeight + 12
            elif newRight == 875:
                player2.getTank().y0 = randHeight + 15
                player2.getTank().y1 = randHeight + 25
                player2.getWeapon().currY = randHeight + 12
            for newTop in range(app.height, randHeight, -25):
                bottom, top = top, newTop
                app.rectangleCoords.append((left, top, right, bottom))
            left, right = right, newRight + 25