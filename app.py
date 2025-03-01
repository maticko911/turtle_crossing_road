import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
timmy = Player()
screen.onkey(timmy.up, "Up")
car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1,6) == 1:
        car.create_car()

    car.move_cars()

    #collision with car
    for cars in car.all_cars:
       if cars.distance(timmy) < 20:
        game_is_on = False
        scoreboard.game_over()

    #detect players finish line
    if timmy.finish_line():
        timmy.go_to_start()
        car.level_up()

screen.exitonclick()



