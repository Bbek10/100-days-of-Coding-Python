import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with car
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful crossing

    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()


    screen.onkey(player.move, "Up")

screen.exitonclick()
