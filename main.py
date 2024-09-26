from turtle import Turtle, Screen
import  random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}

def initiate_turtle(coloration, x, y):
    tim = Turtle(shape="turtle")
    tim.color(coloration)
    tim.penup()
    tim.goto(x, y)
    return tim

for i, color in enumerate(colors):
    turtles[color] = initiate_turtle(colors[i], -230, -90 + (i + 1) * 35)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_color in turtles:
        if turtles[turtle_color].xcor() > 230:
            is_race_on = False
            if turtle_color == user_bet:
                print(f"You've won! The {turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle_color} turtle is the winner!")

        turtles[turtle_color].forward(random.randint(0, 10))

screen.exitonclick()