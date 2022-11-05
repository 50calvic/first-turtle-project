import turtle

def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.left(60)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)


#for i in range(5):
 #   triangle()

def rectangle(edge=100):
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
rectangle()


def ears():
    turtle.circle(25)
    turtle.circle(35)
    turtle.forward(100)
    turtle.circle(25)
    turtle.circle(35)
ears()

def eyes(edge=100):
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    turtle.circle(10)
eyes()



def nose(edge=20):
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.right(120)
    turtle.left(60)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.penup()

nose()

def mouth():
    turtle.right(40)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(20, extent=200)

mouth()

turtle.exitonclick()