import turtle

screen = turtle.Screen()
screen.title('Squares In a Row - PythonTurtle.Academy')
screen.setworldcoordinates(-1000, -1000, 1000, 1000)

turtle.speed(0)
turtle.hideturtle()
turtle.color('purple')


def squaresinarow(x, y, length, n):
    if n == 0: return
    turtle.up()
    turtle.goto(x - length / 2, y - length / 2)
    turtle.down()
    turtle.seth(0)
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)

    squaresinarow(x + 3 * length / 4, y - length / 4, length / 2, n - 1)
    squaresinarow(x - 3 * length / 4, y - length / 4, length / 2, n - 1)


squaresinarow(0, 0, 600, 6)
screen.update()