# import colorgram as color
import random
import turtle as turtle_module

# colors = color.extract('hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#
#
#     rgb_colors.append(new_color)
#
#
#
# print(rgb_colors)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tom = turtle_module.Turtle()
turtle_module.colormode(255)

tom.speed("fastest")
tom.penup()
tom.hideturtle()

tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)
    if  dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
