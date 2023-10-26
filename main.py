import random
from turtle import Turtle, Screen
race_is_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
red = Turtle(shape="turtle")
yellow = Turtle("turtle")
orange = Turtle("turtle")
green = Turtle("turtle")
blue = Turtle("turtle")
purple = Turtle("turtle")
tur = [red, orange, yellow, green, blue, purple]

x = 0
y = -110
for t in tur:
    t.penup()
    t.color(colors[x])
    t.goto(-230, y)
    y += 50
    x += 1


if user_bet:
    race_is_on = True


while race_is_on:
    for t in tur:
        if t.xcor() > 210:
            race_is_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You win. The winner turtle was {winner}")
            else:
                print(f"You lose. The winner turtle was {winner}")
        pace = random.randint(0, 10)
        t.forward(pace)


screen.exitonclick()
