import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



# init objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


# move turtle(player) forward
screen.listen()
screen.onkey(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()

    car_manager.generate_car()
    car_manager.move_left()


    # if player gets to edge of the screen
    if player.ycor() == 280:
        scoreboard.nex_level()
        player.goto(0, -280)

    
    # detect collision with cars and game over
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.penup()
            scoreboard.goto(0, 100)
            scoreboard.write("Sorry, you lost.", align="center", font=("arial", 30, "normal"))
            screen.reset()
            player.hideturtle()
            


    # when player wins
    if scoreboard.level == 5:
        scoreboard.penup()
        scoreboard.goto(0, 100)
        scoreboard.write("Congratulations! You won.", align="center", font=("arial", 30, "normal"))
        screen.reset()
        player.hideturtle()

    
        

    



    
