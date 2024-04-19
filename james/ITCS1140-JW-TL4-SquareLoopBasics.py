import turtle
import random
import time

screen = turtle.Screen()

turtle.setup(800, 800)
turtle.shape('turtle')


# Local variables
colors = ["red", "blue", "yellow", "green"]
teams = ["1111", "2222", "3333", "4444"]
pen_size = int()
speed = int()


# Loop to draw the racers running
for team in range (0, 4):
    # Define Screen Reset
    time.sleep(1)
    turtle.reset()
    pen_size = 1

    # Display team in graphics window
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 300)
    turtle.pencolor('blue')
    turtle.write(teams[team],align="center", font=("Arial", 60, "bold","underline"))
    turtle.pencolor('black')
    turtle.goto(0, 0)
    turtle.pendown()

    for count in range (0, 4):
        speed  = random.randint(1,10)
        #set the pen size and team color
        turtle.color(colors[count])
        turtle.pensize(pen_size)
        turtle.speed(speed)
        #moving the turtle to start
        turtle.penup()
        turtle.goto(0, -300)
        turtle.showturtle()
        turtle.pendown()

        # Draw a square
        turtle.forward(250)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(250)

        pen_size = pen_size + 4

