# This demos using modes (aka screens).

from cmu_112_graphics import *
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

def gameMode_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill='blue')

    for coords in app.rectangleCoords:
        x1,y1,x2,y2 = coords
        canvas.create_rectangle(x1,y1,x2,y2, fill='light green')
    for radius in app.destroyedTerrain:
        x,y = radius
        r = app.baseWeaponR 
        canvas.create_oval(x-r,y-r,x+r,y+r, fill = 'cyan')
    canvas.create_oval(app.currX,app.currY,app.currX+2,app.currY+2, 
                            fill = 'black')
    
    canvas.create_rectangle(playerOne.x0,playerOne.y0,playerOne.x1,playerOne.y1,
                            fill = playerOne.color)
    canvas.create_rectangle(playerTwo.x0,playerTwo.y0,playerTwo.x1,playerTwo.y1,
                            fill = playerTwo.color)
                
    canvas.create_text(app.width/10+15, app.width/8, 
                    text=f'Player One Health \n {playerOne.health}',
                       font='Arial 16 bold', fill='black')
    canvas.create_text(app.width - 60, app.width/8, 
                    text=f'Player Two Health \n {playerTwo.health}',
                       font='Arial 16 bold', fill='black')


def weaponFired(app):
    if app.weaponFired == False:
        return
    else:

        if app.timerMax > 7 and app.timerMax  < 29:

            app.currX = app.currX+app.slope
            app.currY = app.currY+0


        elif app.timerMax > 30:
            
            app.currX = app.currX+app.slope
            app.currY = app.currY+app.slope
        
        else:
            app.currX = app.currX+app.slope
            app.currY = app.currY-app.slope
        

    
    if app.currX > app.width or app.currY < 0:
        app.currX, app.currY = -99999,-99999

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
    startX,startY = 0, 0.8*app.height
    endX,endY = app.width, app.height
    currX1,currY1,currX2,currY2= startX, startY, startX+5, startY+5
    app.rectangleCoords.append((currX1,currY1,currX2,currY2))
    print(int(startY),endY)
    for y in range(int(startY),endY//1,5):
        for x in range(startX,endX,5):
            currX1 = currX1+5
            currY1 = currY1
            currX2 = currX2+5
            currY2 = currY2
            app.rectangleCoords.append((currX1,currY1,currX2,currY2))
        currX1= startX
        currY1, =startY,
        currX2 = startX+5
        currY2= currY2+5
        app.rectangleCoords.append((currX1,currY1,currX2,currY2))
def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))
def gameMode_timerFired(app):
    app.timerMax += 1
    weaponFired(app)
    destroyTerrain(app)
    damageTank(app)

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
    if (event.key == 'Left'):    
        app.weaponFired = True
        gameMode_timerFired(app)
    if (event.key == 'h'):    
        app.mode = 'gameMode'

def damageTank(app):
    x0,y0 = app.currX, app.currY
    if (x0 > (playerTwo.x0) and x0 < playerTwo.x1  and 
            (y0 > playerTwo.y0) and y0 < playerTwo.y1):
            playerTwo.health -= 10
    return playerTwo.health



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
class Tank(object):
    def __init__(self,color,health,player,x0,y0,x1,y1):
        self.color = color
        self.health = health
        self.player = player
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def getHealth(self):
        return self.health
    def getPlayer(self):
        return self.plauer
    def getColor(self):
        return self.color
    def getx0(self):
        return (self.x0)
    def gety0(self):
        return (self.y0)
    def getx1(self):
        return (self.x1)
    def gety1(self):
        return (self.y1)

playerOne = Tank('red',100,True,50,390,75,400)
playerTwo = Tank('purple',100,True,285,390,310,400)
##########################################
# Main App
##########################################

def appStarted(app):
    app.angle =(math.pi)
    app.mode = 'splashScreenMode'
    app.rows = 4
    app.cols = 8
    app.margin = 5 
    app.selection = (-1, -1) 
    app.rectangleCoords = [(200,0,300,app.height)]
    app.destroyedTerrain = []
    app.weaponCoords = []
    app.baseWeaponR = 5
    app.slope = math.sin(app.angle)/math.cos(app.angle)
    app.weaponFired = False
    app.startX,app.startY = playerOne.x1,playerOne.y0
    app.currX,app.currY = app.startX,app.startY
    app.timerMax = -100
    print(math.sin(app.angle),math.cos(app.angle),app.slope)
    createTerrain(app)

def randomizeDot(app):
    app.x = random.randint(20, app.width-20)
    app.y = random.randint(20, app.height-20)
    app.r = random.randint(10, 20)
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
    app.dx = random.choice([+1,-1])*random.randint(3,6)
    app.dy = random.choice([+1,-1])*random.randint(3,6)

def moveDot(app):
    app.x += app.dx
    if (app.x < 0) or (app.x > app.width): app.dx = -app.dx
    app.y += app.dy
    if (app.y < 0) or (app.y > app.height): app.dy = -app.dy

runApp(width=600, height=500)