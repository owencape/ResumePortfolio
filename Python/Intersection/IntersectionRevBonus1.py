import turtle as t
import time




intersection = t.Turtle()


t.Screen().bgcolor("dim gray")
intersection.speed(100)
wn = t.Screen()
wn.addshape("redLight.gif")
wn.addshape("greenLight.gif")
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
    

greenLight=t.Turtle("greenLight.gif")
redLight=t.Turtle("redLight.gif")
greenLight2=t.Turtle("greenLight.gif")
redLight2=t.Turtle("redLight.gif")

def checkForCollision():
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

# def moveUp():
#     white.setheading(90)
#     white.fd(5)
# def moveRight():
#     white.setheading(90)
#     white.fd(5)
# def moveDown():
#     white.setheading(180)
#     white.fd(5)
# def moveLeft():
#     white.setheading(270)
#     white.fd(5)
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
    redLight.hideturtle()
    greenLight2.hideturtle()
    greenLight.penup()
    greenLight2.penup()
    redLight.penup()
    redLight2.penup()
    greenLight.goto(-87,110)
    redLight.goto(-87,110)
    greenLight2.goto(87,-105)
    redLight2.goto(87,-105)


def forwardAllMove():
    red.left(180)
    purple.left(180)
    blue.right(90)
    brown.right(90)
    pink.left(90)
    green.left(90)
    
    
    for i in range(500):
        white.speed(0)
        white.hideturtle()
        white.goto(-400,-15)
        yellow.speed(0)
        yellow.hideturtle()
        yellow.goto(-350,-45)
        red.speed(0)
        red.hideturtle()
        red.goto(460,45)
        purple.speed(0)
        purple.hideturtle()
        purple.goto(375,15)
        brown.speed(0)
        brown.hideturtle()
        brown.goto(-15,450)
        blue.speed(0)
        blue.hideturtle()
        blue.goto(-45,350)
        green.speed(0)
        green.hideturtle()
        green.goto(45,-390)
        pink.speed(0)
        pink.hideturtle()
        pink.goto(15,-450)
        white.showturtle()
        pink.showturtle()
        green.showturtle()
        yellow.showturtle()
        red.showturtle()
        brown.showturtle()
        blue.showturtle()
        purple.showturtle()
        while greenLight.isvisible():
            for i in range (145):
                red.fd(5)
                purple.fd(5)
                
                white.fd(5)
                yellow.fd(5)
                checkForCollision()
            greenLight.hideturtle()
            redLight.showturtle()
            redLight2.hideturtle()
            greenLight2.showturtle()
                
                
        while greenLight2.isvisible():
            
            for i in range(145):
                brown.fd(5)
                blue.fd(5)
                
                pink.fd(5)
                green.fd(5)
                checkForCollision()
            greenLight2.hideturtle()
            redLight2.showturtle()
            redLight.hideturtle()
            greenLight.showturtle()
             

                
# wn.onkeypress(moveUp,"w")
# wn.onkeypress(moveLeft,"a")
# wn.onkeypress(moveDown,"s")
# wn.onkeypress(moveRight,"d")           
        


whiteDashed()
yellowLines()
plusSign()
carPlacement()
forwardAllMove()







wn.listen()
wn.mainloop()