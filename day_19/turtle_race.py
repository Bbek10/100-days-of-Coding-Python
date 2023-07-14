from turtle import Turtle, Screen
import random


color = ["red", "blue", "green", "purple", "indigo", "pink"]
y_axis = [-70, -40, -10, 120, 150,180]
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Enter your bet: ", prompt="Which color Turtle you think will win the race: Enter "
                                                             "Color")
is_race_on = False
all_paddus = []

for turtle_index in range(0,6):
    new_paddu  = Turtle(shape="turtle")
    new_paddu.color(color[turtle_index])
    new_paddu.penup()
    new_paddu.goto(x=-230, y=y_axis[turtle_index])
    all_paddus.append(new_paddu)



if user_bet:
    is_race_on = True

while is_race_on:
    for paddu in all_paddus:
        if paddu.xcor() > 220:
            is_race_on = False
            winning_color = paddu.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} paddu is the WINNER!!!")
            else:
                print(f"You've lost ! The {winning_color} paddu is the WINNER!!!")

        random_movement = random.randint(0, 10)
        paddu.forward(random_movement)






screen.exitonclick()
