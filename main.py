import time
import turtle

import food
import scoreboard
import snake

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(height=630, width=600)
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def boundary():
    """It creates boundary of the playground."""
    bud = turtle.Turtle()
    bud.hideturtle()
    bud.color("white")
    bud.penup()
    bud.goto(280, 280)
    bud.pendown()
    cords = [(-280, 280), (-280, -280), (280, -280), (280, 280)]
    for cor in cords:
        bud.goto(cor)


boundary()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.generate_food()
        scoreboard.increase_score()
        scoreboard.render_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments:
        if segment != snake.head and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
