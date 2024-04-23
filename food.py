import random
import turtle

screen = turtle.Screen()
screen.delay(0)


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.generate_food()

    def generate_food(self):
        """It generates the food."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
