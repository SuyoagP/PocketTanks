# This demos using modes (aka screens).

from cmu_112_graphics import *
from Tank import Tank
from Weapon import *
from Move import *
import random
import math


##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='Welcome to Pocket Tanks',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 200, text='This is the start Screen!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='Press p for the game!',
                       font=font, fill='black')

def splashScreenMode_keyPressed(app, event):
    if (event.key == 'p'):    
        app.mode = 'gameMode'


##########################################
# Game Mode
##########################################
playerOne = Tank('red',100,True,50,390,75,400)
playerTwo = Tank('purple',100,True,285,390,310,400)
newBullet = Bullet(playerOne.getx1(),playerOne.gety0(),45,50, False, 76,390)
newBulletTwo = Bullet(playerTwo.getx0(),playerTwo.gety0(),45,50, False, 285,390)
print(playerTwo.getx0(),playerTwo.gety0())
playerOneMove = Move(playerOne, playerTwo, newBullet,True, 45, 50, False)
playerTwoMove = Move(playerTwo, playerOne, newBulletTwo, False, 45, 50, False)
print(playerOneMove.Move == playerTwo)
def gameMode_redrawAll(app, canvas):
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.image2))

    for coords in app.rectangleCoords:
        x1,y1,x2,y2 = coords
        canvas.create_rectangle(x1,y1,x2,y2, fill='green')
    for radius in app.destroyedTerrain:
        x,y = radius
        r = app.baseWeaponR 
        canvas.create_oval(x-r,y-r,x+r,y+r, fill = 'cyan')
    canvas.create_oval(newBullet.currX, newBullet.currY,newBullet.currX+5,newBullet.currY+2,
                            fill = 'purple')
    canvas.create_oval(newBulletTwo.currX-5, newBulletTwo.currY,newBulletTwo.currX,newBulletTwo.currY+2,
                            fill = 'yellow')
    #canvas.create_image(playerOne.x0, playerOne.y0, image=ImageTk.PhotoImage(app.imageTankOne))
    canvas.create_rectangle(playerOne.x0,playerOne.y0,playerOne.x1,playerOne.y1,
                            fill = playerOne.color)
    canvas.create_rectangle(playerTwo.x0,playerTwo.y0,playerTwo.x1,playerTwo.y1,
                            fill = playerTwo.color)
                
    canvas.create_text(app.width/10+15, app.width/8, 
                    text=f'Player One Health \n {playerOne.health}',
                       font='Arial 16 bold', fill='black')
    canvas.create_text(app.width/10+400, app.width/8,
                    text=f'Player Two Health \n {playerTwo.health}',
                       font='Fixedsys 16 bold', fill='black')
    if playerOneMove.Move == True:
        canvas.create_text(app.width/2 - app.width/4, (app.width/4)*3, text=f'Power : {playerOneMove.power}', font='Arial 16 bold', fill='black')
        canvas.create_text(app.width / 2 + app.width / 4 , (app.width / 4) * 3, text=f'Angle {playerOneMove.angle}', font='Arial 16 bold', fill='black')
    elif playerTwoMove.Move == True:
        canvas.create_text(app.width / 2 - app.width / 4, (app.width / 4) * 3, text=f'Power : {playerTwoMove.power}',font='Arial 16 bold', fill='black')
        canvas.create_text(app.width / 2 + app.width / 4, (app.width / 4) * 3, text=f'Angle {playerTwoMove.angle}',font='Arial 16 bold', fill='black')






def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)
def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)
def createTerrain(app):
    startPoint, startHeight = 0, app.height
    endPoint, endHeight = app.width + 25, int(app.height * (random.randint(0, 6)/10))

    left, right = startPoint, startPoint + 25
    for newRight in range(right, endPoint, 25):

        top, bottom = app.height - 25, app.height
        randHeight = int(app.height * (random.randint(0, 6)/10))

        for newTop in range(app.height, randHeight, -25):
            bottom, top = top, newTop
            app.rectangleCoords.append((left, top, right, bottom))

        left, right = right, newRight + 25

def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def gameMode_timerFired(app):
    if playerOneMove.fire == True:
        app.bulletTimeOne += 0.02
    else: app.bulletTimeOne = 0
    if playerTwoMove.fire == True:
        app.bulletTimeTwo += 0.02
    else: app.bulletTimeTwo = 0
    newBullet.weaponLocation(playerOneMove.angle, playerOneMove.power, app.bulletTimeOne, newBullet.startX,newBullet.startY,app)
    newBulletTwo.weaponLocation(playerTwoMove.angle, playerTwoMove.power, app.bulletTimeTwo, newBulletTwo.startX,newBulletTwo.startY,app)
    destroyTerrain(app)
    if playerTwo.health <= 0:
        app.mode = 'playerOneWin'
    if playerOne.health <= 0:
        app.mode = 'playerTwoWin'
    if playerOneMove.Move == True:
        playerOneMove.executeMove(playerTwoMove)
    if playerTwoMove.Move == True:
        playerTwoMove.executeMove(playerOneMove)


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
            newBulletTwo.fire = True
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
    app.image1 = app.loadImage('Sunrise.png')
    app.image2 = app.scaleImage(app.image1, 2 / 3)
    app.imageTankOne = app.loadImage('TankOne.jpeg')
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
    createTerrain(app)





runApp(width=600, height=500)