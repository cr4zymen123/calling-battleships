####################################
# Calling Battleships by Omar Khan #
#         January 8th, 2024        #
####################################
    
from tkinter import *
from math import *  #only if you need sqrt, pi, sin, cos or tan
from time import *
from replit import audio

root = Tk()
screen = Canvas(root, width=800, height=600, background="darkgreen")

#screen.creates for background/static objects...
def setInitialValues():
  #global variables...
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1, x1Ship2, y1Ship2, x2Ship2, y2Ship2, Ship2, maxSpeed, velocity1, velocity2, shots, xShot, yShot, shotSpeed, ship1Health, ship2Health, shotCooldown, mainMenu, shotHitShip2, velocity3, velocity4, endGame, ship2Move, ship2MoveSpeed, shotHitShip1, shotCooldown2, shots2, xShot2, yShot2
  
  #Ship1 size, coordinates and shot variables with their arrays
  x1Ship1 = 385
  y1Ship1 = 530
  x2Ship1 = 415
  y2Ship1 = 580
  ship1Health = 5
  maxSpeed = 7
  velocity1 = 0
  velocity2 = 0
  velocity3 = 0
  velocity4 = 0
  shots = []
  xShot = []
  yShot = []
  shotSpeed = 27 #How fast the shots go
  shotCooldown = False

  #Ship2 size, coordinates and shot variables with their arrays
  x1Ship2 = 385
  y1Ship2 = 20
  x2Ship2 = 415
  y2Ship2 = 70
  ship2Health = 10
  shotCooldown2 = False
  shots2 = []
  xShot2 = []
  yShot2 = []

  #Other game initial variables
  mainMenu = True
  endGame = False
  shotHitShip1 = False
  shotHitShip2 = False
  ship2Move = True
  ship2MoveSpeed = 5


#Importing the audio soundtrack
  global backgroundAudio
  backgroundAudio = audio.play_file("soundtrack.mp3")
  

def drawMainMenu():
  global mainMenuText, mainMenuCanvas, gameTitle, mainMenuInstructions, mainMenuInstructions2, mainMenuInstructions3, controlsText, controlsBackgroud, titleBackgroud
  
  mainMenuCanvas = screen.create_rectangle(0, 0, 800, 600, fill = "forestgreen")
  titleBackgroud = screen.create_rectangle(140,40,650,110, fill = "lightslategrey", width = 7, outline = "slategrey")
  controlsBackgroud = screen.create_rectangle(100,375,700,580, fill = "lightslategrey", width = 7, outline = "slategrey")
  gameTitle = screen.create_text(400, 75, text = "Calling Battleships", fill = "green", font = "Roman 34 bold")
  mainMenuText = screen.create_text(400, 280, text = "Click Anywhere To Play", fill = "white", font = "Roman 26 bold")

  controlsText = screen.create_text(400, 400, text = "CONTROLS", fill = "black", font = "Roman 14 bold")
  mainMenuInstructions = screen.create_text(400, 450, text = "Use the arrow keys to move your tank below the border.", fill = "black",font = "Roman 14")
  mainMenuInstructions2 = screen.create_text(400, 500, text = "Use the '1' key to shoot the tank.", fill = "black", font = "Roman 14")
  mainMenuInstructions3 = screen.create_text(400, 550, text = "Your objective is to destroy the tank above the border!", fill = "black", font = "Roman 14")

    

def drawObjects():
   #screen.creates for animated objects...
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1, x1Ship2, y1Ship2, x2Ship2, y2Ship2, Ship2, Ship1HealthDisplay, Ship2HealthDisplay, Ship1HealthInt, Ship2HealthInt, borderline, Ship1Canon, Ship1Head, Ship1Enterance, Ship1Detail, Ship2Canon, Ship2Head, Ship2Enterance, Ship2Detail, rock, mudPuddle
  
  #Ship1 graphics
  Ship1 = screen.create_rectangle(x1Ship1, y1Ship1, x2Ship1, y2Ship1, fill = "red", width = 3)
  Ship1Canon = screen.create_oval(x1Ship1 + 10, y1Ship1-7, x2Ship1-12, y2Ship1-25, fill = "maroon")
  Ship1Head = screen.create_oval(x1Ship1 + 2, y1Ship1+12, x2Ship1-3, y2Ship1-1, fill = "firebrick")
  Ship1Enterance = screen.create_oval(x1Ship1 + 10, y1Ship1+20, x2Ship1-6, y2Ship1-14, fill = "indianred")
  Ship1Detail = screen.create_rectangle(x1Ship1 + 6,y1Ship1+34,x2Ship1-17,y2Ship1-8, fill = "dimgrey")
  
  #Ship2 graphics
  Ship2 = screen.create_rectangle(x1Ship2, y1Ship2, x2Ship2, y2Ship2, fill = "blue", width = 3)
  Ship2Canon = screen.create_oval(x1Ship2 + 12, y1Ship2+8, x2Ship2-10, y2Ship2+7, fill = "darkblue")
  Ship2Head = screen.create_oval(x1Ship2 + 2, y1Ship2+1, x2Ship2-3, y2Ship2-12, fill = "mediumblue")
  Ship2Enterance = screen.create_oval(x1Ship2 + 10, y1Ship2+20, x2Ship2-6, y2Ship2-14, fill = "royalblue")
  Ship2Detail = screen.create_rectangle(x1Ship2 + 10,y1Ship2+17,x2Ship2-12,y2Ship2-26, fill = "dimgrey")

  #Other graphics
  Ship1HealthDisplay = screen.create_text(60,580, text = "Health:", fill = "black", font = "Ariel 18 bold")
  Ship2HealthDisplay = screen.create_text(60,20, text = "Health:", fill = "black", font = "Ariel 18 bold")
  Ship1HealthInt = screen.create_text(125,580, text = ship1Health, fill = "black", font = "Ariel 18 bold")
  Ship2HealthInt = screen.create_text(125,20, text = ship2Health, fill = "black", font = "Ariel 18 bold")
  borderline = screen.create_rectangle(0, 290, 800, 310, fill = "black")
  rock = screen.create_oval(120,220,150,250, fill = "grey")
  mudPuddle = screen.create_oval(650,500,700,550, fill = "saddlebrown")


def updateObjects():
  #increment statements/absolute updating...
  global ship2Move, ship2MoveSpeed, x1Ship2, x2Ship2, y1Ship2, y2Ship2

  if ship2Move:
    #Moving Ship2 horizontally
    x1Ship2 += ship2MoveSpeed
    x2Ship2 += ship2MoveSpeed

    #Checking if Ship2 hits the boundaries
    if x1Ship2 <= 0 or x2Ship2 >= 800:
      ship2MoveSpeed = -ship2MoveSpeed
    
  
def mouseClickHandler( event ):
  global mainMenu
  #code to run on click...
  if mainMenu == True:
    mainMenu = False

#Checking if Ship1 and Ship2 hit the borderline or the sides. This prevents the Ships from 
def checkForCollisions():
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1, x1Ship2, y1Ship2, x2Ship2, y2Ship2, Ship2, maxSpeed, velocity1, velocity2, ship2TakeDamage, shotHitShip2, ship2Health, xShot
  #Ship 1 borders
  if x1Ship1 <= 0:
    x1Ship1 = 0
    x2Ship1 = 30
  if x2Ship1 >= 800:
    x1Ship1 = 770
    x2Ship1 = 800
  if y1Ship1 <= 310:
    y1Ship1 = 310
    y2Ship1 = 360
  if y2Ship1 >= 600:
    y1Ship1 = 550
    y2Ship1 = 600

  #Ship 2 borders
  if x1Ship2 <= 0:
    x1Ship2 = 0
    x2Ship2 = 30
  if x2Ship2 >= 800:
    x1Ship2 = 770
    x2Ship2 = 800
  if y1Ship2 <= 0:
    y1Ship2 = 0
    y2Ship2 = 50
  if y2Ship2 >= 290:
    y1Ship2 = 240
    y2Ship2 = 290

#Takes health away from Ship1
def ship1TakeDamage():
  global ship1Health, shotHitShip1, x1Ship1, y1Ship1, x2Ship1, y2Ship1, shots2

  for i in range(len(yShot2)):
    if xShot2[i] + 20 >= x1Ship1 and xShot2[i] <= x2Ship1 and yShot2[i] + 10 >= y1Ship1 and yShot2[i] <= y2Ship1:
      if not shotHitShip1:
        shotHitShip1 = True
        ship1Health -= 1

#Takes health away from Ship2
def ship2TakeDamage():
  global ship2Health, shotHitShip2, x1Ship2, y1Ship2, x2Ship2, y2Ship2, shots
  
  for i in range(len(yShot)):
    if xShot[i] + 20 >= x1Ship2 and xShot[i] <= x2Ship2 and yShot[i] + 10 >= y1Ship2 and yShot[i] <= y2Ship2:
      if not shotHitShip2:
        shotHitShip2 = True
        ship2Health -= 1


#code to run on key press...
def keyDownHandler(event):
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1, maxSpeed, velocity1, velocity2, shotCooldown, lastShotTime

  currentTime = time()
  if event.keysym == "Left":
    #Subtract velocity (decreasing in the x axis means going left)
    velocity1 = -maxSpeed
  
  if event.keysym == "Right":
    #Add velocity (increasing in the x axis means going right)
    velocity1 = maxSpeed
    
  if event.keysym == "Up":
    #Subtract velocity (decreasing in the y axis means going right)
    velocity2 = -maxSpeed
  
  if event.keysym == "Down":
    #Add velocity (increasing in the y axis means going down)
    velocity2 = maxSpeed

  if event.keysym == "1" and (currentTime - lastShotTime) > 1:
    #Call the spawn new shot function
    spawnNewShot()
    #Resets the current time as the last shot time
    lastShotTime = currentTime
    #Triggering the shot cooldown
    shotCooldown = False


#When a key is lifted up
def keyUpHandler(event):
  global velocity1, velocity2
  
  velocity1 = 0
  velocity2 = 0
    
#Updating the Ship1 coordinates to display
def updateShip1Position():
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1
  
  x1Ship1 = x1Ship1 + velocity1
  x2Ship1 = x2Ship1 + velocity1
  y1Ship1 = y1Ship1 + velocity2
  y2Ship1 = y2Ship1 + velocity2

#Updating the Ship2 coordinates to display
def updateShip2Position():
  global x1Ship2, y1Ship2, x2Ship2, y2Ship2, velocity3, velocity4, Ship2

  x1Ship2 = x1Ship2 + velocity3
  x2Ship2 = x2Ship2 + velocity3
  y1Ship2 = y1Ship2 + velocity4
  y2Ship2 = y2Ship2 + velocity4

#Updating shot coordinates to display
def updateShotPositions():
  global shots, xShot, yShot, ship2Health
  for i in range(0, len(yShot)):
    yShot[i] = yShot[i] - shotSpeed
    ship2TakeDamage()

  deleteOffScreenShots()

#Updating shot2 coordinates to display
def updateShot2Positions():
  global shots2, xShot2, yShot2, ship1Health
  for i in range(0, len(yShot2)):
    yShot2[i] = yShot2[i] + shotSpeed
    ship1TakeDamage()

  deleteOffScreenShots2()

  
#Deleting the shot when it passes the screen
def deleteOffScreenShots():
  global shotCooldown
  i = 0
  
  while i < len(yShot)-1:
    if yShot[i] < 0 and shotCooldown == True:
      yShot.pop(i)
      xShot.pop(i)
      shots.pop(i)
      shotCooldown = False
    else:
      i = i + 1
      
#Deleting shot2 when it passes the screen
def deleteOffScreenShots2():
  global shotCooldown2
  i = 0

  while i < len(yShot2)-1:
    if yShot2[i] < 0 and shotCooldown2 == True:
      yShot2.pop(i)
      xShot2.pop(i)
      shots2.pop(i)
      shotCooldown2 = False
    else:
      i = i + 1

#Displaying the shot
def drawShot():
  for i in range(len(yShot)):
    shots[i] = screen.create_oval(xShot[i] + 10, yShot[i] - 5, xShot[i] + 20, yShot[i] + 5, fill = "yellow")

def deleteShot():
  for i in range(len(yShot)):
    screen.delete(shots[i])

#Displaying the shot
def drawShot2():
  for i in range(len(yShot2)):
    shots2[i] = screen.create_oval(xShot2[i] + 10, yShot2[i] - 5, xShot2[i] + 20, yShot2[i] + 5, fill = "yellow")

def deleteShot2():
  for i in range(len(yShot2)):
    screen.delete(shots2[i])


#Spawning a new shot from Ship1
def spawnNewShot():
  global shots, xShot, yShot, shotSpeed, shotCooldown, shotHitShip2

  #If the cooldown time has passed
  if not shotCooldown:
    shotCooldown = True
    #Finding the coordinates of the ship to spawn the shot in front of the ship
    xShot.append( x1Ship1 )
    yShot.append( y1Ship1 )
    shots.append(0)
    shotHitShip2 = False


#Spawning a shot from Ship2 and make it shoot every second
def ship2Shoot():
  global shots2, xShot2, yShot2, ship2Health, lastShotTime2, currentTime2, x2Ship2, y2Ship2, shots2, shotHitShip1

  currentTime2 = time()

  #This line checks if the most recent shot is 2 seconds old
  if currentTime2 - lastShotTime2 > 2:
    xShot2.append(x2Ship2 - 28)
    yShot2.append(y2Ship2 + 5)
    shots2.append(0)
    shotHitShip1 = False
    lastShotTime2 = currentTime2
    

def youLostFunction():
  global endGame, x1Ship1, y1Ship1

  ship1Explosion = screen.create_polygon(x2Ship1 - 30, y2Ship1 - 35, x2Ship1 - 10, y2Ship1 - 45, x2Ship1 + 30, y2Ship1 - 45, x2Ship1 + 50, y2Ship1 - 40, x2Ship1+35, y2Ship1-10, x2Ship1+25,y2Ship1,x2Ship1+20,y2Ship1+35, x2Ship1, y2Ship1+15, x2Ship1-25, y2Ship1+45,x2Ship1-35,y2Ship1+8,x2Ship1-55,y2Ship1+10,x2Ship1-40,y2Ship1-15, x2Ship1 - 50,y2Ship1 - 45, x2Ship1 - 15,y2Ship1 - 55, x2Ship1 - 20, y2Ship1 - 40, fill = "orange")

  screen.update()
  sleep(6)
  endGameCanvas = screen.create_rectangle(0, 0, 800, 600, fill = "black")
  endGameText = screen.create_text(400, 200, text = "You Lost", fill = "red", font = "Roman 32 bold")
  screen.update()
  #Shows the lose screen for 5 seconds, then resets the game by bringing back the start menu
  sleep(5)
  screen.delete(endGameCanvas, endGameText, ship1Explosion)
  endGame = False
  runGame()
  

def youWinFunction():
  global endGame, x1Ship1, x2Ship1, y1Ship1, y2Ship2, x1Ship2, y1Ship2, x2Ship2, y2Ship2, Ship2

  
  ship2Explosion = screen.create_polygon(x2Ship2 - 30, y2Ship2 - 35, x2Ship2 - 10, y2Ship2 - 45, x2Ship2 + 30, y2Ship2 - 45, x2Ship2 + 50, y2Ship2 - 40, x2Ship2+35, y2Ship2-10, x2Ship2+25,y2Ship2,x2Ship2+20,y2Ship2+35, x2Ship2, y2Ship2+15, x2Ship2-25, y2Ship2+45,x2Ship2-35,y2Ship2+8,x2Ship2-55,y2Ship2+10,x2Ship2-40,y2Ship2-15, x2Ship2 - 50,y2Ship2 - 45, x2Ship2 - 15,y2Ship2 - 55, x2Ship2 - 20, y2Ship2 - 40, fill = "orange")
  
  screen.delete(Ship2)
  screen.update()
  sleep(6)
  endGameCanvas = screen.create_rectangle(0, 0, 800, 600, fill = "black")
  endGameText = screen.create_text(400, 200, text = "You Win! ez clap.", fill = "green", font = "Roman 32 bold")
  screen.update()
  #Shows the win screen for 5 seconds, then resets the game by bringing back the start menu
  sleep(5)
  screen.delete(endGameCanvas, endGameText, ship2Explosion)
  endGame = False
  runGame()

#Running the game
def runGame():
  #Bringing all of the global variables to run in the game
  global x1Ship1, y1Ship1, x2Ship1, y2Ship1, velocity1, velocity2, Ship1, x1Ship2, y1Ship2, x2Ship2, y2Ship2, Ship2, shot, xShot, yShot, ship1Health, ship2Health, lastShotTime, lastShotTime2, mainMenuText, mainMenuCanvas, mainMenu, gameTitle, mainMenuInstructions, mainMenuInstructions2, mainMenuInstructions3, Ship1HealthDisplay, Ship2HealthDisplay, Ship1HealthInt, Ship2HealthInt, borderline, ship2Move, endGame, youLostFunction, youWinFunction, ship2Shoot, lastShotTime2, currentTime2, Ship1Canon, Ship1Head, Ship1Enterance, Ship1Detail, Ship2Canon, Ship2Head, Ship2Enterance, Ship2Detail, backgroundAudio, controlsBackgroud, titleBackgroud, rock, mudPuddle
  
  setInitialValues() 
  lastShotTime = time()
  lastShotTime2 = time()

  while not endGame:

    if mainMenu == True:
      drawMainMenu()
      screen.update()
      sleep(0.03)
      screen.delete(mainMenuText, mainMenuCanvas, gameTitle, mainMenuInstructions, mainMenuInstructions2, mainMenuInstructions3, controlsText, controlsBackgroud, titleBackgroud)
      
    else:
      
      drawObjects()
      
      #Updating Ship1 shot coordinates on screen
      updateShotPositions()
      #Updating Ship2 shot coordinates on screen
      updateShot2Positions()
      #Updating the Ship1 coordinates on screen
      updateShip1Position()
      #Updating the Ship2 coordinates on screen
      updateShip2Position()
      drawShot()
      ship2Shoot()
      drawShot2()
      #Creating a frame per second system by updating what to display on the screen
      screen.update()
      sleep(0.03)
      screen.delete(Ship1, Ship2, Ship1HealthDisplay, Ship1HealthInt, Ship2HealthDisplay, Ship2HealthInt, borderline, Ship1Canon, Ship1Head, Ship1Enterance, Ship1Detail, Ship2Canon, Ship2Head, Ship2Enterance, Ship2Detail, rock, mudPuddle)

      updateObjects()  
      deleteShot()
      deleteShot2()
      #Creating barriers for the game so the ships cant go off screen or cross the black line
      checkForCollisions()
    
      
        
      # stopGame()
      if ship1Health <= 0 and endGame == False:
        sleep(1)  #Adding a one second delay for dramatic effect
        audio.play_file("explosion.mp3")
        endGame = True
        backgroundAudio.set_paused(True)
        youLostFunction()
        screen.delete("all")  #Removing everything from the screen
        
      elif ship2Health <= 0 and endGame == False:
        sleep(1)  #Adding a one second delay for dramatic effect
        audio.play_file("explosion.mp3")
        endGame = True
        backgroundAudio.set_paused(True)
        youWinFunction()
        screen.delete("all")  #Removing everything from the screen
        


#Call the runGame function
root.after( 0, runGame )

#Connecting user inputs to functions
screen.bind( "<Button-1>", mouseClickHandler )
screen.bind( "<Key>", keyDownHandler )
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
screen.focus_set()
root.mainloop()