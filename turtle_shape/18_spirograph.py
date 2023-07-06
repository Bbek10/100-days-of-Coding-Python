import random

import turtle as  t
import random

angle = [0, 90, 180, 270]
tom = t.Turtle()
t.colormode(255)



tom.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color




def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(10)


screen = t.Screen()
screen.exitonclick()