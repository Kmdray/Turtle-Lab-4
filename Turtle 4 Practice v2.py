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

# Function to get input and set landscape/environment
# TODO: get # teams, colors. draw racetrack, finish line

def get_input():
    """Gets number of teams and colors from user."""
    n_teams = int(input("Enter number of teams: "))
    colors_allowed = [
            (255, 0, 0),  # red
            (0, 255, 0),  # green
            (0, 0, 255),  # blue
            (255, 165, 0)  # orange
        ]
    # TODO: are speeds decided here, are they random?
    teams = [
            # (laps_completed, distance_covered, color)
            (0, 0.0, "red") for _ in range(n_teams)
        ]
    return teams

# functions to perform laps, relays, size changes, etc.

# functions to decide winner, display results, etc.

# Main function
def main():
    # get input (number of teams) from user
    teams = get_input()
    print(teams)
    exit()

    # Set up the screen
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
