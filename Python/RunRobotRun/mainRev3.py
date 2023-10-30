#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveUp():
  robot.setheading(90)
  robot.fd(50)
def moveDown():
  robot.setheading(270)
  robot.fd(50)
def moveLeft():
  robot.setheading(180)
  robot.fd(50)
def moveRight():
  robot.setheading(0)
  robot.fd(50)
#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''
def firstLevel():
  for i in range(4):
    move()
  for i in range(3):
    turn_left()
  for i in range(4):
    move()
  robot.clear()
  

def secondLevel():
  robot.color("red")
  turn_left()
  for i in range(3):
    move()
  for i in range(3):
    turn_left()
  for i in range(2):
    move()
  robot.clear()
  
    
def thirdLevel():
  robot.color("green")
  turn_left()
  for i in range(2):
    move()
    for k in range(3):
      turn_left()
    move()
    turn_left()
  robot.color("pink")
  for i in range(2):
    move()
    for k in range(3):
        turn_left()
    move()
    turn_left()
  robot.clear()

def fourthLevel():
    robot.color("gold")
    move()
    for i in range(3):
        turn_left()
    for i in range(4):
        move()
    turn_left()
    for i in range(2):
        move()
    robot.clear()
        
    

while True:
  firstLevel()
  robot.goto(-100,-100)
  wn.bgpic("maze2.png")
  secondLevel()
  robot.goto(-100,-100)
  wn.bgpic("maze3.png")
  thirdLevel()
  robot.goto(-100,-100)
  wn.bgpic("maze4.png")
  fourthLevel()
  robot.goto(-100,-100)
  wn.bgpic("maze1.png")
  robot.color("purple")
# ui=input("w,a,s,d")
# actions={"w":moveUp(),
#          "a":moveLeft(),
#          "s":moveDown(),
#          "d":moveRight()
         
# }

  



#---- end robot movement 

wn.mainloop()
