# This demos using modes (aka screens).
from Game.Player import Player
from Weapon import *
from Game.Move import *
import random
import math
from tkinter import Tk, font
from Graphics import *
from Params import *



#Template Taken from CMU 112 Website

##########################################
# Main App
##########################################
def appStarted(app):
    # Image https://opengameart.org/content/morning-sunrise-background
    # Method found via Course Notes
    app.timerDelay = 0
    app.destroyedTerrain = []
    app.TankOneY, app.TankTwoY = app.height, app.height
    #https://play.google.com/store/apps/details?id=com.blitwise.ptankshd&hl=en_US&gl=US
    app.startScreenBackGroundImage = app.loadImage('../Assets/PTSS.gif')
    app.startScreenBackGroundImage = app.scaleImage(app.startScreenBackGroundImage, 4)
    app.planetImage = app.loadImage('../Assets/ptanks.icns')
    app.planetImage = app.scaleImage(app.planetImage, 0.6)
    app.image1 = app.loadImage('../Assets/GameBackGroundGradient.jpeg')
    app.image2 = app.scaleImage(app.image1, 5)
    app.tankImageOne = app.loadImage('../Assets/pixel-tank-removebg-previewOne.png')
    app.tankImageTwo = app.loadImage('../Assets/pixel-tank-removebg-previewTwo.png')
    app.playerOneTurn = True
    app.angle =(math.pi)
    app.mode = 'splashScreenMode'
    app.rectangleCoords = []
    app.weaponFired = False
    app.startX,app.startY = player1.getTank().x1,player1.getTank().y0
    app.currX,app.currY = app.startX,app.startY
    app.bulletTimeOne = 0
    app.bulletTimeTwo = 0
    Graphics.createTerrain(app)





def splashScreenMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0,app.width,app.height, fill='black')
    #image found here: https://www.google.com/url?sa=i&url=https%3A%2F%2Fplaceit.net%2Fc%2Fvideos%2Fstages%2Ftwitch-offline-screen-video-maker-with-an-8-bit-style-and-city-graphics-3853&psig=AOvVaw1JVAZw1M26CXq3YOnky7du&ust=1669676524573000&source=images&cd=vfe&ved=0CBAQ3YkBahcKEwiwzLjyu8_7AhUAAAAAHQAAAAAQBA
    backGroundImage = app.startScreenBackGroundImage
    backGroundImage = app.scaleImage(backGroundImage, 2/3)
    canvas.create_image(app.width/2, app.height/4, image=ImageTk.PhotoImage(backGroundImage))
    canvas.create_image(app.width / 2, 3 * app.height / 4, image=ImageTk.PhotoImage(app.planetImage))
    canvas.create_text(8.5*app.width / 10, 9.5 * app.height / 10,
                      text='Press P to Play!', font='Futura 40', fill='white')







def splashScreenMode_keyPressed(app, event):
    if (event.key == 'p'):    
        app.mode = 'gameMode'


##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    graphicsEngine = Graphics(app, canvas)
    graphicsEngine.createBackground()
    graphicsEngine.updateTerrain()
    graphicsEngine.createBulletRight(player1.getWeapon(), 'red')
    graphicsEngine.createBulletLeft(player2.getWeapon(), 'blue')
    graphicsEngine.createTankOne(player1.getTank())
    graphicsEngine.createTankTwo(player2.getTank())
    graphicsEngine.createPlayerHealth(-1*app.width/30, player1.getTank().health, 'One')
    graphicsEngine.createPlayerHealth(7.8*app.width/10, player2.getTank().health, 'Two')
    graphicsEngine.createPlayerPowerAngle(player1,player2)





def gameMode_timerFired(app):
    app.timerDelay += 1
    if app.timerDelay >= 0.1:
        app.timerDelay = 0

        if (player1.getTurn() == True and player1.getLockedTurn() == True):


            player1.getWeapon().weaponFireOne(player1.getWeapon().angle, player1.getWeapon().power, 0, player1.getTank().x1, player1.getTank().y0-3, app, player2.getTank().x0,player2.getTank().y0,player2.getTank().x1, player2.getTank().y1)

            if (player1.getWeapon().outOfBounds == True or player1.getWeapon().tankHit == True or player1.getWeapon().terrainHit == True):

                if player1.getWeapon().tankHit == True:
                    player2.getTank().health -= player1.getWeapon().damage



                player1.getWeapon().outOfBounds = False
                player1.getWeapon().tankHit = False
                player1.getWeapon().terrainHit = False

                player1.setLockedTurn(False)
                player1.setTurn(False)
                player2.setTurn(True)


        elif(player2.getTurn() == True and player2.getLockedTurn() == True):
            player2.getWeapon().weaponFireTwo(player2.getWeapon().angle, player2.getWeapon().power, 0, player2.getTank().x0, player2.getTank().y0-3, app, player1.getTank().x0,player1.getTank().y0,player1.getTank().x1, player1.getTank().y1)

            if (player2.getWeapon().outOfBounds == True or player2.getWeapon().tankHit == True or player2.getWeapon().terrainHit == True):


                if player2.getWeapon().tankHit == True:
                    player1.getTank().health -= player2.getWeapon().damage

                player2.getWeapon().outOfBounds = False
                player2.getWeapon().tankHit = False
                player2.getWeapon().terrainHit = False

                player2.setLockedTurn(False)
                player2.setTurn(False)
                player1.setTurn(True)




    if player2.getTank().health <= 0:
        app.mode = 'pOneWin'
        player1.getTank().health = 20
        player2.getTank().health = 20
    elif player1.getTank().health <= 0:
        app.mode = 'pTwoWin'
        player1.getTank().health = 20
        player2.getTank().health = 20


def gameMode_mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    app.destroyedTerrain.append((app.cx,app.cy))



def gameMode_keyPressed(app, event):
    #Fire Weapon
    if (event.key == 'f'):

        if (player1.getTurn() == True and player1.getLockedTurn() == False):
            player1.setLockedTurn(True)
            player1.getWeapon().time = 0

        elif player2.getTurn() == True and player2.getLockedTurn() == False:
            player2.setLockedTurn(True)
            player2.getWeapon().time = 0

    if (event.key == 'h'):
        app.mode = 'helpMode'

    #Increase Angle
    elif (event.key == 'Up'):
        if player1.getTurn() == True:
            player1.getWeapon().angle += 1
        elif player2.getTurn() == True:
            player2.getWeapon().angle += 1

    #Decrease Angle
    elif (event.key == 'Down'):
        if player1.getTurn() == True:
            player1.getWeapon().angle -= 1
        elif player2.getTurn() == True:
            player2.getWeapon().angle -= 1

    #Increase Power
    elif (event.key == 'w'):
        if player1.getTurn() == True:
            player1.getWeapon().power += 1
        elif player2.getTurn() == True:
            player2.getWeapon().power += 1

    #Decrease Power
    elif (event.key == 's'):
        if player1.getTurn() == True:
            player1.getWeapon().power -= 1
        elif player2.getTurn() == True:
            player2.getWeapon().power -= 1

    #Toggle Bullet
    if (event.key == '1'):
        if (player1.turn == True):
            player1.weapon = Bullet(player1.getTank().getx1(), player1.getTank().gety0(), 45, 50, False, 76, 390)
        elif (player2.turn == True):
            player2.weapon = Bullet(player2.getTank().getx1(), player2.getTank().gety0(), 45, 50, False, 285, 390)

    #Toggle MountainMover
    elif (event.key == '2'):
        if (player1.turn == True):
            player1.weapon = MountainMover(player1.getTank().getx1(), player1.getTank().gety0(), 45, 50, False, 76, 390)
        elif (player2.turn == True):
            player2.weapon = MountainMover(player2.getTank().getx1(), player2.getTank().gety0(), 45, 50, False, 285, 390)

    #Toggle MagicWall
    elif (event.key == '3'):
        if (player1.turn == True):
            player1.weapon = MagicWall(player1.getTank().getx1(), player1.getTank().gety0(), 45, 50, False, 76, 390)
        elif (player2.turn == True):
            player2.weapon = MagicWall(player2.getTank().getx1(), player2.getTank().gety0(), 45, 50, False, 285, 390)
##########################################
# Player Two Win Screen
##########################################
def pOneWin_redrawAll(app, canvas):
    font = 'Futura 36'
    canvas.create_text(app.width/2, 150, text='Player One Wins',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='Congrats!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350,
                        text='Press any key to return to the game!',
                       font=font, fill='black')
def pOneWin_keyPressed(app, event):
    app.mode = 'splashScreenMode'
##########################################
# Player Two Win Screen
##########################################
def pTwoWin_redrawAll(app, canvas):
    font = 'Futura 36'
    canvas.create_text(app.width/2, 150, text='Player Two Wins!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='Congrats!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350,
                        text='Press any key to return to the game!',
                       font=font, fill='black')
def pTwoWin_keyPressed(app, event):
    app.mode = 'splashScreenMode'


##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas):
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.image2))
    canvas.create_text(app.width / 2, app.height / 15,
                            text='How To Play', font='Futura 40', fill='white')
    canvas.create_text(app.width / 2,1.5* app.height / 10,
                            text='Use the Up and Down arrow keys to change the angle of your shot', font='Futura 25', fill='white')
    canvas.create_text(app.width / 2, 2.5* app.height / 10,
                            text='Use the W and S keys to change the Power of your shot', font='Futura 25', fill='white')
    canvas.create_text(app.width / 2, 3.5* app.height / 10,
                            text='Use the 1,2,3 keys to toggle between the Bullet, the Mountain Mover, and the Magic Wall', font='Futura 25', fill='white')
    canvas.create_text(app.width / 2, 4.5* app.height / 10,
                            text='Press any Key to return to the Game', font='Futura 40', fill='white')
def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'






runApp(width=1200, height=1000)