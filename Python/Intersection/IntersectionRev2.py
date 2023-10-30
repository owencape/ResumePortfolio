import turtle as t



intersection = t.Turtle()


t.Screen().bgcolor("dim gray")
intersection.speed(100)
wn = t.Screen()
def yellowLines():
    
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

def forwardAllMove():
    red.left(180)
    purple.left(180)
    blue.right(90)
    brown.right(90)
    pink.left(90)
    green.left(90)
    for i in range(300):
        red.fd(2)
        purple.fd(2)
        
        blue.fd(2)
        brown.fd(2)
        
        pink.fd(2)
        green.fd(2)
        
        white.fd(2)
        yellow.fd(2)
    















whiteDashed()
yellowLines()
plusSign()
carPlacement()
forwardAllMove()







wn.mainloop()