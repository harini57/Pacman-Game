import turtle
import random

food_x = random.randint(-200, 200)
food_y = random.randint(-200, 200)
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.setpos(food_x, food_y)

turtle.register_shape("down_pacman.gif")
turtle.register_shape("left_pacman.gif")
turtle.register_shape("right_pacman.gif")
turtle.register_shape("up_pacman.gif")
pacman = turtle.Turtle()
pacman.penup()
pacman.shape("right_pacman.gif")

screen = turtle.Screen()

score_counter = 0


def score(score_counter):
    score_counter += 1
    print(score_counter)


def up():
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15) and \
            (food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        food.setpos(food_x, food_y)
        food.showturtle()
        score(score_counter)
    pacman.shape("up_pacman.gif")
    pacman.setheading(90)
    pacman.forward(10)


def down():
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15) and \
            (food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        food.setpos(food_x, food_y)
        food.showturtle()
        score(score_counter)
    pacman.shape("down_pacman.gif")
    pacman.setheading(270)
    pacman.forward(10)


def left():
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15) and \
            (food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        food.setpos(food_x, food_y)
        food.showturtle()
        score(score_counter)
    pacman.shape("left_pacman.gif")
    pacman.setheading(180)
    pacman.forward(10)


def right():
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15) and \
            (food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        food.setpos(food_x, food_y)
        food.showturtle()
        score(score_counter)
    pacman.shape("right_pacman.gif")
    pacman.setheading(0)
    pacman.forward(10)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

turtle.done()
