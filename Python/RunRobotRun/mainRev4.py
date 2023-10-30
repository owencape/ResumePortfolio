#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
move = True

def levelUp():
  global level
  
  if robot.xcor() == 100 and (robot.ycor() == 100) and level==1:
    robot.clear()
    robot.goto(-100,-100)
    wn.bgpic("maze2.png")
    robot.color("yellow")
    level+=1
  elif robot.xcor() == 0 and (robot.ycor() == 50) and level ==2:
    robot.clear()
    robot.goto(-100,-100)
    wn.bgpic("maze3.png")
    robot.color("red")
    level+=1
  elif robot.xcor() == 0 and (robot.ycor() == 0) and level == 3:
    robot.color("green")
  elif robot.xcor() == 100 and (robot.ycor() == 100) and level == 3: 
    robot.clear()
    robot.goto(-100,-100)
    wn.bgpic("maze4.png")
    robot.color("blue")
    level+=1
  elif robot.xcor() == 100 and (robot.ycor() == 50) and level == 4: 
    robot.clear()
    print("You win")

level=1
def moveUp():
  global level
  global move
  if robot.xcor() == 100 and (robot.ycor() == -100) and level==2 or robot.xcor() == -50 and (robot.ycor() == -50) and level==2 or robot.xcor() == 0 and (robot.ycor() == -50) and level==2 or robot.xcor() == 100 and (robot.ycor() == -50) and level==2 or robot.xcor() == -50 and (robot.ycor() == 0) and level==2 or robot.xcor() == 0 and (robot.ycor() == 0) and level==2 or robot.xcor() == -100 and (robot.ycor() == 100) and level==2 or robot.xcor() == 0 and (robot.ycor() == 100) and level==2 or robot.xcor() == 100 and (robot.ycor() == 100) and level==2 or robot.xcor() == -50 and (robot.ycor() == 100) and level==2 or  robot.xcor() == 0 and (robot.ycor() == -100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==3 or robot.xcor() == 100 and (robot.ycor() == -50) and level==3 or robot.xcor() == 100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 50) and level==3 or robot.xcor() == -50 and (robot.ycor() == 100) and level==3 or robot.xcor() == 0 and (robot.ycor() == 100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==4 or robot.xcor() == 0 and (robot.ycor() == 0) and level==4 or robot.xcor() == -100 and (robot.ycor() == 50) and level==4 or robot.xcor() == 50 and (robot.ycor() == 50) and level==4 or robot.xcor() == 100 and (robot.ycor() == 100) and level==4:
    robot.goto(-100,-100)
  
  robot.setheading(90)
  robot.fd(50)
  robot.dot(10)
  
  levelUp()
  

  
def moveDown():
  global level
  global move
  if robot.xcor() == 100 and (robot.ycor() == -100) and level==2 or robot.xcor() == -50 and (robot.ycor() == -50) and level==2 or robot.xcor() == 0 and (robot.ycor() == -50) and level==2 or robot.xcor() == 100 and (robot.ycor() == -50) and level==2 or robot.xcor() == -50 and (robot.ycor() == 0) and level==2 or robot.xcor() == 0 and (robot.ycor() == 0) and level==2 or robot.xcor() == -100 and (robot.ycor() == 100) and level==2 or robot.xcor() == 0 and (robot.ycor() == 100) and level==2 or robot.xcor() == 100 and (robot.ycor() == 100) and level==2 or robot.xcor() == -50 and (robot.ycor() == 100) and level==2 or  robot.xcor() == 0 and (robot.ycor() == -100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==3 or robot.xcor() == 100 and (robot.ycor() == -50) and level==3 or robot.xcor() == 100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 50) and level==3 or robot.xcor() == -50 and (robot.ycor() == 100) and level==3 or robot.xcor() == 0 and (robot.ycor() == 100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==4 or robot.xcor() == 0 and (robot.ycor() == 0) and level==4 or robot.xcor() == -100 and (robot.ycor() == 50) and level==4 or robot.xcor() == 50 and (robot.ycor() == -50) and level==4 or robot.xcor() == 100 and (robot.ycor() == 100) and level==4:
    robot.goto(-100,-100)
  else:
    move == True
  if move == False:
    pass
  elif move == True:
    robot.setheading(270)
    robot.fd(50)
    robot.dot(10)
  levelUp()
    
def moveLeft():
  global level
  global move
  if robot.xcor() == 100 and (robot.ycor() == -100) and level==2 or robot.xcor() == -50 and (robot.ycor() == -50) and level==2 or robot.xcor() == 0 and (robot.ycor() == -50) and level==2 or robot.xcor() == 100 and (robot.ycor() == -50) and level==2 or robot.xcor() == -50 and (robot.ycor() == 0) and level==2 or robot.xcor() == 0 and (robot.ycor() == 0) and level==2 or robot.xcor() == -100 and (robot.ycor() == 100) and level==2 or robot.xcor() == 0 and (robot.ycor() == 100) and level==2 or robot.xcor() == 100 and (robot.ycor() == 100) and level==2 or robot.xcor() == -50 and (robot.ycor() == 100) and level==2 or  robot.xcor() == 0 and (robot.ycor() == -100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==3 or robot.xcor() == 100 and (robot.ycor() == -50) and level==3 or robot.xcor() == 100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 50) and level==3 or robot.xcor() == -50 and (robot.ycor() == 100) and level==3 or robot.xcor() == 0 and (robot.ycor() == 100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==4 or robot.xcor() == 0 and (robot.ycor() == 0) and level==4 or robot.xcor() == -100 and (robot.ycor() == 50) and level==4 or robot.xcor() == 50 and (robot.ycor() == -50) and level==4 or robot.xcor() == 100 and (robot.ycor() == 100) and level==4:
    robot.goto(-100,-100)
  else:
    move == True
  if move == False:
    pass
  elif move == True:
    robot.setheading(180)
    robot.fd(50)
    robot.dot(10)
  levelUp()
    
def moveRight():
  global level
  global move
  if robot.xcor() == 100 and (robot.ycor() == -100) and level==2 or robot.xcor() == -50 and (robot.ycor() == -50) and level==2 or robot.xcor() == 0 and (robot.ycor() == -50) and level==2 or robot.xcor() == 100 and (robot.ycor() == -50) and level==2 or robot.xcor() == -50 and (robot.ycor() == 0) and level==2 or robot.xcor() == 0 and (robot.ycor() == 0) and level==2 or robot.xcor() == -100 and (robot.ycor() == 100) and level==2 or robot.xcor() == 0 and (robot.ycor() == 100) and level==2 or robot.xcor() == 100 and (robot.ycor() == 100) and level==2 or robot.xcor() == -50 and (robot.ycor() == 100) and level==2 or  robot.xcor() == 0 and (robot.ycor() == -100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==3 or robot.xcor() == 100 and (robot.ycor() == -50) and level==3 or robot.xcor() == 100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 50) and level==3 or robot.xcor() == -50 and (robot.ycor() == 100) and level==3 or robot.xcor() == 0 and (robot.ycor() == 100) and level==3 or robot.xcor() == 50 and (robot.ycor() == -100) and level==4 or robot.xcor() == 0 and (robot.ycor() == 0) and level==4 or robot.xcor() == -100 and (robot.ycor() == 50) and level==4 or robot.xcor() == 50 and (robot.ycor() == -50) and level==4 or robot.xcor() == 100 and (robot.ycor() == 100) and level==4:
    robot.goto(-100,-100)
  else:
    move == True
  if move == False:
    pass
  elif move == True:
    robot.setheading(0)
    robot.fd(50)
    robot.dot(10)
  levelUp()
  
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

# pos = robot.pos()
# curX = int(pos[0])
# curY = int(pos[1])


# if robot.xcor() == 100 and (robot.ycor() == -100) and level==3 or robot.xcor() == -50 and (robot.ycor() == -50) and level==2 or robot.xcor() == 0 and (robot.ycor() == -50) and level==2 or robot.xcor() == 100 and (robot.ycor() == -50) and level==2 or robot.xcor() == -50 and (robot.ycor() == 0) and level==2 or robot.xcor() == 0 and (robot.ycor() == 0) and level==2 or robot.xcor() == -100 and (robot.ycor() == 100) and level==2 or robot.xcor() == 0 and (robot.ycor() == 100) and level==2 or robot.xcor() == 100 and (robot.ycor() == 100) and level==2 or robot.xcor() == -50 and (robot.ycor() == 100) and level==2:
# if robot.xcor() == -50 and (robot.ycor() == -50) and level==2:
# if robot.xcor() == 0 and (robot.ycor() == -50) and level==2:
# if robot.xcor() == 100 and (robot.ycor() == -50) and level==2:
# if robot.xcor() == -50 and (robot.ycor() == 0) and level==2:
# if robot.xcor() == 0 and (robot.ycor() == 0) and level==2:
# if robot.xcor() == -100 and (robot.ycor() == 100) and level==2:
# if robot.xcor() == 0 and (robot.ycor() == 100) and level==2:
# if robot.xcor() == 100 and (robot.ycor() == 100) and level==2:
# if robot.xcor() == -50 and (robot.ycor() == 100) and level==2:

# if robot.xcor() == 0 and (robot.ycor() == -100) and level==4 or robot.xcor() == 50 and (robot.ycor() == -100) and level==3 or robot.xcor() == 100 and (robot.ycor() == -50) and level==3 or robot.xcor() == 100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 0) and level==3 or robot.xcor() == -100 and (robot.ycor() == 50) and level==3 or robot.xcor() == -50 and (robot.ycor() == 100) and level==3 or robot.xcor() == 0 and (robot.ycor() == 100) and level==3

# if robot.xcor() == 50 and (robot.ycor() == -100) and level==4 or robot.xcor() == 0 and (robot.ycor() == 0) and level==4 or robot.xcor() == -100 and (robot.ycor() == 50) and level==4 or robot.xcor() == 50 and (robot.ycor() == -50) and level==4 or robot.xcor() == 100 and (robot.ycor() == 100) and level==4:



  
wn.onkeypress(moveUp,"w")
wn.onkeypress(moveLeft,"a")
wn.onkeypress(moveDown,"s")
wn.onkeypress(moveRight,"d")




#---- end robot movement 
wn.listen()
wn.mainloop()
