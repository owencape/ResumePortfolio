import turtle as t

t.Screen().bgcolor("dim gray")
t.speed(100)
wn = t.Screen()
def yellowLines():
    
    #right line
    t.right(180)
    t.penup()
    t.goto(75,0)
    t.pendown()
    t.color("yellow")
    t.pensize(4)
    t.forward(330)
    #left line
    t.penup()
    t.goto(-75,0)
    t.left(180)
    t.pendown()
    t.color("yellow")
    t.pensize(4)
    t.forward(330)
    #top line
    t.penup()
    t.goto(0,75)
    t.right(90)
    t.pendown()
    t.color("yellow")
    t.pensize(4)
    t.forward(260)
    #bottom line
    t.penup()
    t.goto(0,-75)
    t.right(180)
    t.pendown()
    t.color("yellow")
    t.pensize(4)
    t.forward(260)
    
    
def whiteDashed():
    #left bottom
    t.penup()
    t.goto(-30,-90)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #right bottom
    t.left(90)
    t.penup()
    t.goto(30,-90)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #right top
    t.left(180)
    t.penup()
    t.goto(90,30)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #bottom right
    t.left(90)
    t.penup()
    t.goto(90,-30)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #top left
    t.left(180)
    t.penup()
    t.goto(-30,90)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #top right
    t.left(90)
    t.penup()
    t.goto(30,90)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #bottom left
    t.left(180)
    t.penup()
    t.goto(-90,-30)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    #left top
    t.left(90)
    t.penup()
    t.goto(-90,30)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.color("white")
    for i in range(6):
        t.forward(25)
        t.penup()
        t.forward(20)
        t.pendown()
    
def plusSign():
    #top right
    t.left(90)
    t.color("black")
    t.pensize(6)
    t.penup()
    t.goto(70,70)
    t.pendown()
    t.forward(350)
    t.goto(70,70)
    t.left(90)
    t.forward(350)
    #bottom left
    t.left(90)
    t.penup()
    t.goto(-70,-70)
    t.pendown()
    t.forward(300)
    t.goto(-70,-70)
    t.left(90)
    t.forward(350)
    #top left
    t.right(90)
    t.penup()
    t.goto(-70,70)
    t.pendown()
    t.forward(350)
    t.goto(-70,70)
    t.right(90)
    t.forward(350)
    #bottom right
    t.right(90)
    t.penup()
    t.goto(70,-70)
    t.pendown()
    t.forward(350)
    t.goto(70,-70)
    t.right(90)
    t.forward(350)



whiteDashed()
yellowLines()
plusSign()



wn.mainloop()