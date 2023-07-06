import random

import turtle as  t
import random

angle = [0, 90, 180, 270]
tom = t.Turtle()
t.colormode(255)


tom.pensize(10)
tom.speed("fast")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color





for move in range(300):
    tom.forward(30)
    tom.setheading(random.choice(angle))

    tom.color(random_color())


screen = t.Screen()
screen.exitonclick()