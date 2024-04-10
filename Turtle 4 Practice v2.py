import turtle
import random

# Function to create a turtle with specific color and speed
def create_turtle(color, speed):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color)
    t.speed(speed)
    return t

# Function to move the turtle forward
def move_forward(t):
    t.forward(100)

# Main function
def main():
    turtle.setup(width=800, height=600)
    turtle.bgcolor("yellow")
    turtle.title("Turtle Relay Race")

    colors = ["red", "green", "blue", "orange"]
    # Speeds corresponding to colors
    speeds = [1, 2, 3, 4]  

    # Create turtles with specific colors and speeds
    turtles = [create_turtle(color, speed)
    for color, speed in zip(colors, speeds)]

    # Set starting positions
    for i, t in enumerate(turtles):
        t.penup()
        t.goto(-350, -100 + i * 50)
        t.pendown()

    # Race loop
    laps = 4
    for lap in range(1, laps + 1):
        print(f"Lap {lap}:")
        for t in turtles:
            move_forward(t)
            if t.xcor() >= 350:
                # Change turtle color and reset position
                t.color(random.choice(colors))
                t.speed(speeds[colors.index(t.color())])
                t.goto(-350, -100 + colors.index(t.color()) * 50)

    turtle.done()

if __name__ == "__main__":
    main()
