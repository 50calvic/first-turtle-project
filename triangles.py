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


for i in range(5):
    triangle()
