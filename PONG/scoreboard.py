from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def end(self):
        if self.r_score == 10:
            self.goto(0, 0)
            self.write("Right Paddle wins", align="center", font=("Courier", 40, "normal"))

        elif self.l_score == 10:
            self.goto(0, 0)
            self.write("Left Paddle wins", align="center", font=("Courier", 40, "normal"))

            


