import turtle as t




intersection = t.Turtle()


t.Screen().bgcolor("dim gray")
intersection.speed(100)
wn = t.Screen()
def yellowLines():
    intersection.speed(0)
    #right line
    intersection.right(180)
    intersection.penup()
    intersection.goto(75,0)
    intersection.pendown()
    intersection.color("yellow")
    intersection.pensize(4)
    intersection.forward(330)
    #left line
    intersection.penup()
    intersection.goto(-75,0)
    intersection.left(180)
    intersection.pendown()
    intersection.color("yellow")
    intersection.pensize(4)
    intersection.forward(330)
    #top line
    intersection.penup()
    intersection.goto(0,75)
    intersection.right(90)
    intersection.pendown()
    intersection.color("yellow")
    intersection.pensize(4)
    intersection.forward(260)
    #bottom line
    intersection.penup()
    intersection.goto(0,-75)
    intersection.right(180)
    intersection.pendown()
    intersection.color("yellow")
    intersection.pensize(4)
    intersection.forward(260)
    
    
def whiteDashed():
    intersection.speed(0)
    #left bottom
    intersection.penup()
    intersection.goto(-30,-90)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #right bottom
    intersection.left(90)
    intersection.penup()
    intersection.goto(30,-90)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #right top
    intersection.left(180)
    intersection.penup()
    intersection.goto(90,30)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #bottom right
    intersection.left(90)
    intersection.penup()
    intersection.goto(90,-30)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #top left
    intersection.left(180)
    intersection.penup()
    intersection.goto(-30,90)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #top right
    intersection.left(90)
    intersection.penup()
    intersection.goto(30,90)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #bottom left
    intersection.left(180)
    intersection.penup()
    intersection.goto(-90,-30)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    #left top
    intersection.left(90)
    intersection.penup()
    intersection.goto(-90,30)
    intersection.right(90)
    intersection.pendown()
    intersection.pensize(3)
    intersection.color("white")
    for i in range(6):
        intersection.forward(25)
        intersection.penup()
        intersection.forward(20)
        intersection.pendown()
    
def plusSign():
    intersection.speed(0)
    #top right
    intersection.left(90)
    intersection.color("black")
    intersection.pensize(6)
    intersection.penup()
    intersection.goto(70,70)
    intersection.pendown()
    intersection.forward(350)
    intersection.goto(70,70)
    intersection.left(90)
    intersection.forward(350)
    #bottom left
    intersection.left(90)
    intersection.penup()
    intersection.goto(-70,-70)
    intersection.pendown()
    intersection.forward(300)
    intersection.goto(-70,-70)
    intersection.left(90)
    intersection.forward(350)
    #top left
    intersection.right(90)
    intersection.penup()
    intersection.goto(-70,70)
    intersection.pendown()
    intersection.forward(350)
    intersection.goto(-70,70)
    intersection.right(90)
    intersection.forward(350)
    #bottom right
    intersection.right(90)
    intersection.penup()
    intersection.goto(70,-70)
    intersection.pendown()
    intersection.forward(350)
    intersection.goto(70,-70)
    intersection.right(90)
    intersection.forward(350)

def moveUp():
    white.setheading(0)
    white.fd(5)
def moveRight():
    white.setheading(270)
    white.fd(5)
def moveDown():
    white.setheading(180)
    white.fd(5)
def moveLeft():
    white.setheading(90)
    white.fd(5)
wn.addshape("redX.gif")
wn.addshape("yellowCar.gif")
wn.addshape("greenCar.gif")
wn.addshape("pinkCar.gif")
wn.addshape("redCar.gif")
wn.addshape("blueCar.gif")
wn.addshape("purpleCar.gif")
wn.addshape("whiteCar.gif")
wn.addshape("brownCar.gif")
yellow=t.Turtle("yellowCar.gif")
green=t.Turtle("greenCar.gif")
pink=t.Turtle("pinkCar.gif")
red=t.Turtle("redCar.gif")
blue=t.Turtle("blueCar.gif")
purple=t.Turtle("purpleCar.gif")
white=t.Turtle("whiteCar.gif")
brown=t.Turtle("brownCar.gif")
def carPlacement():
    white.penup()
    white.goto(-250,-15)
    yellow.penup()
    yellow.goto(-200,-45)
    red.penup()
    red.goto(310,45)
    purple.penup()
    purple.goto(225,15)
    brown.penup()
    brown.goto(-15,300)
    blue.penup()
    blue.goto(-45,200)
    green.penup()
    green.goto(45,-240)
    pink.penup()
    pink.goto(15,-300)

allCars=[white,yellow,red,purple,brown,blue,green,pink]
move = True
def forwardAllMove():
    global move
    red.left(180)
    purple.left(180)
    blue.right(90)
    brown.right(90)
    pink.left(90)
    green.left(90)
    while move == True:
                wn.onkeypress(moveUp,"w")
                wn.onkeypress(moveLeft,"a")
                wn.onkeypress(moveDown,"s")
                wn.onkeypress(moveRight,"d") 
                red.fd(5)
                purple.fd(5)
                
                blue.fd(5)
                brown.fd(5)
                
                pink.fd(5)
                green.fd(5)
                
                
                yellow.fd(5)
                
                if abs(yellow.xcor() - green.xcor()) < 30 and abs(yellow.ycor() - green.ycor()) < 30:
                    print("collided")
                    yellow.shape("redX.gif")
                    yellow.stamp()
                    yellow.hideturtle()
                    green.hideturtle()
                if abs(white.xcor() - blue.xcor()) < 30 and abs(white.ycor() - blue.ycor()) < 30:
                    print("collided")
                    white.shape("redX.gif")
                    white.stamp()
                    blue.hideturtle()
                    white.speed(0)
                    white.hideturtle()
                    white.goto(1000,1000)
                if abs(brown.xcor() - purple.xcor()) < 30 and abs(brown.ycor() - purple.ycor()) < 30:
                    print("collided")
                    brown.shape("redX.gif")
                    brown.stamp()
                    purple.hideturtle()
                    brown.speed(0)
                    brown.hideturtle()
                    brown.goto(1000,1000)
                if abs(red.xcor() - pink.xcor()) < 30 and abs(red.ycor() - pink.ycor()) < 30:
                    print("collided")
                    red.shape("redX.gif")
                    red.stamp()
                    pink.hideturtle()
                    red.speed(0)
                    red.hideturtle()
                    red.goto(1000,1000)
                wn.listen()
    move = False
                
        
        


whiteDashed()
yellowLines()
plusSign()
carPlacement()
forwardAllMove()








wn.mainloop()