from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_level()
        
        

    
    def update_level(self):
        self.write(f"Level {self.level}", align="center", font=(FONT))

    

    def nex_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=(FONT))
        self.move_speed *= 0.6
