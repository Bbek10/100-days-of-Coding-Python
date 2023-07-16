import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek Game")
screen.tracer(0)

snek = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect Collision with Food
    if snek.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snek.extend()
        score.score_increment()
    # Detect Collision with wall
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    # Detect Collision with tail
    for segment in snek.segments[1:len(snek.segments):1]: # [1::] works as well
        # if segment == snek.head:
        #     pass
        if snek.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # If head collides with any segment in the tail trigger game over

    # Slicing Concept Ccmmented if is for non -sliced



screen.exitonclick()
