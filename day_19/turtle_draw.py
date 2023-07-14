from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def clockwise():
    tom.right(10)


def counter_clockwise():
    tom.left(10)


def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
