import turtle as t
from turtle import Screen
import random

colors = ["medium blue","green yellow","magenta","deep pink","coral","maroon","indigo"]

tom = t.Turtle()
tom.shape("turtle")


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tom.forward(100)
        tom.right(angle)


for shape_side_n in range(3, 10):
    tom.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
