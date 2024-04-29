import turtle
import random
import time

posponer = 0.1
score = 0
high_score = 0

# Settings de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# food
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0 High Score: 0", align="center",
            font=("Courier", 24, "normal"))

# body of the snake
segments = []


def up():
    cabeza.direction = "up"


def down():
    cabeza.direction = "down"


def left():
    cabeza.direction = "left"


def right():
    cabeza.direction = "right"


def move():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Teclado
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

while True:
    wn.update()

    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        texto.clear()
        texto.write("Score: {} High Score: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)
        score += 1
        if score > high_score:
            high_score = score
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segments.append(nuevo_segmento)

        texto.clear()
        texto.write("Score: {} High Score: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segments[0].goto(x, y)

    move()

    #colision with the body snake
    for segment in segments:
        if segment.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            texto.clear()
            texto.write("Score: {} High Score: {}".format(score, high_score), align="center",
                        font=("Courier", 24, "normal"))

    time.sleep(posponer)
