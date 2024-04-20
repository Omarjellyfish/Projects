import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

screen = turtle.Screen()
screen.title('ssssnaaake')
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.tracer(0)

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('blue')
snake.up()
snake.goto(0, 0)
snake.direction = 'stop'

# food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.up()
food.goto(0, 100)

segments = []

# scoreboard

sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('black')
sc.up()
sc.hideturtle()
sc.goto(0, 260)
sc.write('Score:0   HighScore:0', align='center', font=('ds-digital', 24, 'normal'))


def moveup():
    if snake.direction != 'down':
        snake.direction = 'up'


def movedown():
    if snake.direction != 'up':
        snake.direction = 'down'


def moveright():
    if snake.direction != 'left':
        snake.direction = 'right'


def moveleft():
    if snake.direction != 'right':
        snake.direction = 'left'


def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)


screen.listen()
screen.onkeypress(moveup, 'w')
screen.onkeypress(movedown, 's')
screen.onkeypress(moveright, 'd')
screen.onkeypress(moveleft, 'a')

# mainloop
while True:
    screen.update()

    # creating collision
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = 'stop'
        for segment in segments:
            segment.goto(1000, 1000)  # out of range

        segments.clear()

        score = 0

        delay = 0.1
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        sc.clear()
        sc.write('score: {} Highscore: {}'.format(score, high_score), align='center', font=('ds-digital', 24, 'normal'))

    # eating food
    if snake.distance(food) < 20:
        # move the food to random location and increase score:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.up()
        segments.append(new_segment)

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write('score: {} Highscore: {}'.format(score, high_score), align='center', font=('ds-digital', 24, 'normal'))

    # moving the segments in reverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # move segment zero to snake
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()
    # colision with segments/body
    for segment in segments:
        if segment.distance(snake) < 20:
            x = random.randint(-290, 290)#place food in another random location
            y = random.randint(-290, 290)#place food in another random location
            food.goto(x, y) #place food in another random location
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = 'stop'
            # delete body / hide it
            for segment in segments:#deleting all segments
                segment.goto(1000, 1000)
            segments.clear()#clearing the list
            score = 0
            delay = 0.1


            # update scoreboard again
            sc.clear()
            sc.write('score: {} Highscore: {}'.format(score, high_score), align='center',font=('ds-digital', 24, 'normal'))
    time.sleep(delay)

