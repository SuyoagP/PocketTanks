# This demos using modes (aka screens).

from Weapon import *
from Game.Move import *
import random
import math
from tkinter import Tk, font
from Graphics import *
from Params import *



#Template Taken from CMU 112 Website

def splashScreenMode_redrawAll(app, canvas):
    #image found here: https://www.google.com/url?sa=i&url=https%3A%2F%2Fplaceit.net%2Fc%2Fvideos%2Fstages%2Ftwitch-offline-screen-video-maker-with-an-8-bit-style-and-city-graphics-3853&psig=AOvVaw1JVAZw1M26CXq3YOnky7du&ust=1669676524573000&source=images&cd=vfe&ved=0CBAQ3YkBahcKEwiwzLjyu8_7AhUAAAAAHQAAAAAQBA
    backGroundImage = app.startScreenBackGroundImage
    backGroundImage = app.scaleImage(backGroundImage, 2/3)
    canvas.create_image(app.width/2, app.height/4, image=ImageTk.PhotoImage(backGroundImage))

    buttonleft,buttonTop,buttonRight,buttonBottom = (app.width/4, 6*app.height/10,3*app.width/4,7*app.width/10)
    font = 'Arial 26'
    canvas.create_text(app.width/2, 200, text='This is the start Screen!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='Press p for the game!',
                       font=font, fill='black')
    canvas.create_rectangle(buttonleft, buttonTop, buttonRight, buttonBottom, fill='blue', outline='black')






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
    graphicsEngine.createBulletRight(newBullet, 'red')
    graphicsEngine.createBulletLeft(newWeaponTwo, 'blue')
    graphicsEngine.createTank(playerOne)
    graphicsEngine.createTank(playerTwo)
    graphicsEngine.createPlayerHealth(15, playerOne, 'One')
    graphicsEngine.createPlayerHealth(400, playerTwo, 'Two')



newBullet = Bullet(playerOne.getx1(), playerOne.gety0(), 45, 50, False, 76, 390)
playerOneMove = Move(playerOne, playerTwo, newBullet, True, 45, 50, False)


def gameMode_timerFired(app):
    if playerOneMove.fire == True:
        app.bulletTimeOne += 0.02
    else: app.bulletTimeOne = 0
    if playerTwoMove.fire == True:
        app.bulletTimeTwo += 0.02
    else: app.bulletTimeTwo = 0
    newBullet.weaponLocation(playerOneMove.angle, playerOneMove.power, app.bulletTimeOne, newBullet.startX, newBullet.startY, app)
    newWeaponTwo.weaponLocation(playerTwoMove.angle, playerTwoMove.power, app.bulletTimeTwo, newWeaponTwo.startX, newWeaponTwo.startY, app)
    destroyTerrain(app)
    if playerTwo.health <= 0:
        app.mode = 'playerOneWin'
    if playerOne.health <= 0:
        app.mode = 'playerTwoWin'
    if playerOneMove.Move == True:
        playerOneMove.executeMove(playerTwoMove)
        newBullet.destroyTerrain(app)
    if playerTwoMove.Move == True:
        playerTwoMove.executeMove(playerOneMove)
    newBullet.destroyTerrain(app)


def gameMode_mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    app.destroyedTerrain.append((app.cx,app.cy))
def destroyTerrain(app):
    for block in app.rectangleCoords:
        x0,y0,x1,y1 = block
        if (app.currX > min(x0,x1) 
        and app.currX < max(x0,x1)) and (app.currY > 
                min(y0,y1) and app.currY < max(y0,y1)):
                app.rectangleCoords.remove(block)
    return app.rectangleCoords


def gameMode_keyPressed(app, event):
    if (event.key == 'f'):
        if playerOneMove.Move == True:
            newBullet.fire = True
            playerOneMove.fire = True
        if playerTwoMove.Move == True:
            newWeaponTwo.fire = True
            playerTwoMove.fire = True
    if (event.key == 'h'):
        app.mode = 'helpMode'
    if (event.key == 'Up'):
        if playerOneMove.fire == False and playerOneMove.Move == True:
            playerOneMove.angle += 1
            print(playerOneMove.angle)
        elif playerTwoMove.fire == False and playerTwoMove.Move == True:
            playerTwoMove.angle += 1
            print(playerTwoMove.angle)
    if (event.key == 'Down'):
        if playerOneMove.fire == False and playerOneMove.Move == True:
            playerOneMove.angle -= 1
            print(playerOneMove.angle)
        elif playerTwoMove.fire == False and playerTwoMove.Move == True:
            playerTwoMove.angle -= 1
            print(playerTwoMove.angle)
    if (event.key == 'w'):
        if playerOneMove.fire == False and playerOneMove.Move == True:
            playerOneMove.power += 1
            print(playerOneMove.angle)
        elif playerTwoMove.fire == False and playerTwoMove.Move == True:
            playerTwoMove.power += 1
            print(playerTwoMove.power)
    if (event.key == 's'):
        if playerOneMove.fire == False:
            playerOneMove.power -= 1
            print(playerOneMove.angle)
        elif playerTwoMove.fire == False and playerTwoMove.Move == True:
            playerTwoMove.power -= 1
            print(playerTwoMove.power)
    if (event.key == 'p') and playerOneMove.Move == True:
            newBullet = MountainMover(playerOne.getx1(), playerOne.gety0(), 45, 50, False, 76, 390)
            print('mountain')
            print(newBullet.terrainDestroy)



def pOneWin_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='Player One Win',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='(Insert helpful message here)',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350,
                        text='Press any key to return to the game!',
                       font=font, fill='black')

def helpMode_keyPressed(app, event):
    app.mode = 'splashScreenMode'

##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='This is the help screen!', 
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='(Insert helpful message here)',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350, 
                        text='Press any key to return to the game!',
                       font=font, fill='black')

def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'



##########################################
# Main App
##########################################

def appStarted(app):
    # Image https://opengameart.org/content/morning-sunrise-background
    # Mthod found via Course Notes
    app.startScreenBackGroundImage = app.loadImage('../Assets/Pocket-Tanks.png')
    app.image1 = app.loadImage('../Assets/Sunrise.png')
    app.image2 = app.scaleImage(app.image1, 2 / 3)
    app.imageTankOne = app.loadImage('../Assets/TankOne.jpeg')
    app.playerOneTurn = True
    app.angle =(math.pi)
    app.mode = 'splashScreenMode'
    app.selection = (-1, -1) 
    app.rectangleCoords = []
    app.destroyedTerrain = []
    app.weaponCoords = []
    app.baseWeaponR = 5
    app.weaponFired = False
    app.startX,app.startY = playerOne.x1,playerOne.y0
    app.currX,app.currY = app.startX,app.startY
    app.bulletTimeOne = 0
    app.bulletTimeTwo = 0
    Graphics.createTerrain(app)


runApp(width=600, height=500)