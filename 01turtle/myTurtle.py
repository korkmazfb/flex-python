import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.fillcolor("white")
turtle.begin_fill()

for x in range(36):
    turtle.forward(30)
    turtle.right(40)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50)
    turtle.right(200)
    turtle.forward(100)
    turtle.left(5)

turtle.end_fill()
turtle.done()