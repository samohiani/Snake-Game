from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 370)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score = {self.score}', align=ALIGNMENT, move=False, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER!', align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
