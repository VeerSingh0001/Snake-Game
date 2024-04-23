import turtle

screen = turtle.Screen()

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.render_score()

    def render_score(self):
        """It renders the score on the screen"""
        self.write(arg=f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """It updates the score as snake eat the food."""
        self.clear()
        self.score += 1

    def game_over(self):
        """It shows the game over dialog on screen when a game over."""
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
