#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:46:15 2024 -0400

Title: Turtle Relay Race

Description:    This program simulates a relay race between multiple teams using the
                turtle module.

@authors: Kevin, Shane, James, Matt
"""
import random
import sys
import time
import turtle

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Constants
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N_LANES = 6
N_RELAYS = 4

WIDTH = 800
HEIGHT = 600

PADDING_TOP = 50
PADDING_BOTTOM = 150
PADDING_LEFT = 50
PADDING_RIGHT = 100

WIDTH_TRACK = WIDTH - PADDING_LEFT - PADDING_RIGHT
HEIGHT_TRACK = HEIGHT - PADDING_TOP - PADDING_BOTTOM
HEIGHT_LANE = HEIGHT_TRACK / N_LANES
WIDTH_RELAY = WIDTH_TRACK / N_RELAYS

TRACK_START_X = -WIDTH / 2 + PADDING_LEFT
TRACK_END_X = TRACK_START_X + WIDTH_TRACK
TRACK_START_Y = -HEIGHT / 2 + PADDING_BOTTOM
TRACK_END_Y = TRACK_START_Y + HEIGHT_TRACK

FONT_SIZE_LANE_LABELS = 12
PADDING_LANE_LABEL = 25

COLORS_ALLOWED = [
    ("red"),  # red
    ("green"),  # green
    ("blue"),  # blue
    ("orange"),  # orange
    ("yellow"),  # yellow
    ("purple"),  # purple
]
NAMES_ALLOWED = [
    "scarlet speedsters",
    "green machines",
    "blue blazers",
    "orange ocelots",
    "yellow yaks",
    "purple panthers",
]
SPEEDS_ALLOWED = [
  random.randint(1,10),
  random.randint(1,10),
  random.randint(1,10),
  random.randint(1,10),
  random.randint(1,10),
  random.randint(1,10),
]
TIMES_TAKEN = [
    0,
    0,
    0,
    0,
    0,
    0,
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Input & setup functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_scenery(n_teams):
    """
    Sets up the racetrack and finish line.
    @authors: Shane
    """
    turtle.setup(width=WIDTH, height=HEIGHT)
    turtle.bgcolor("lightblue")
    turtle.title("Turtle Relay Race")

    # Draw rectangular racetrack perimeter
    turtle.penup()
    turtle.goto(TRACK_START_X, TRACK_START_Y)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(5)
    turtle.forward(WIDTH_TRACK)
    turtle.left(90)
    turtle.forward(HEIGHT_TRACK)
    turtle.left(90)
    turtle.forward(WIDTH_TRACK)
    turtle.left(90)
    turtle.forward(HEIGHT_TRACK)
    turtle.left(90)

    # Draw relay exchange zones
    turtle.color("red")
    turtle.pensize(1)
    for i in range(N_RELAYS - 1):  # 3 lines make 4 relay zones
        turtle.penup()
        turtle.goto(
            TRACK_START_X + (i + 1) * WIDTH_RELAY,
            [TRACK_START_Y, TRACK_END_Y][i % 2],
        )
        turtle.pendown()
        turtle.goto(
            TRACK_START_X + (i + 1) * WIDTH_RELAY,
            [TRACK_END_Y, TRACK_START_Y][i % 2],
        )

    # Label lane numbers with team index
    # TODO: use team color? (Shane)
    turtle.color("black")
    for i in range(0, n_teams):
        turtle.penup()
        turtle.goto(
            TRACK_START_X - PADDING_LANE_LABEL,
            lane_n_center_y_pos(i) - FONT_SIZE_LANE_LABELS,
        )
        turtle.pendown()
        turtle.write(i, font=("Arial", FONT_SIZE_LANE_LABELS, "normal"))

    # Draw lanes
    turtle.color("black")
    turtle.pensize(2)
    for i in range(N_LANES - 1):  # 5 lines make 6 lanes
        turtle.penup()
        turtle.goto(
            [TRACK_START_X, TRACK_END_X][i % 2],
            TRACK_START_Y + (i + 1) * HEIGHT_LANE,
        )
        turtle.pendown()
        turtle.forward(WIDTH_TRACK)
        turtle.left(180)

    # Hide cursor
    turtle.hideturtle()


def get_input_for_number_of_teams():
    """
    Gets number of teams from user input.
    @authors: Shane
    """
    # Get number of teams
    n_teams = int(input("Enter number of teams, between 2 and 6: "))

    # Verify it's between two and six
    if n_teams < 2 or n_teams > 6:
        raise ValueError("Number of teams must be between 2 and 6.")

    return n_teams


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def lane_n_center_y_pos(n):
    """
    Returns the y-coordinate of the center of the nth lane. NOTE: starts at 0.
    @authors: Shane
    """
    return TRACK_START_Y + HEIGHT_LANE / 2 + n * HEIGHT_LANE


def create_turtle(color):
    """
    Function to create a turtle with specific color.
    @authors: Kevin
    """
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    return t


def move_forward(t):
    """
    Function to move the turtle forward by 100 units.
    @TODO: remove this, it's an unused function now.
    @authors: Kevin
    """
    t.forward(100)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main race/relay function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_race(TEAMS):
    # Local variables
    trtl_speed = int()
    trtl_height = float()
    trtl_width = float()
    pen_size = int()

    # Create stopwatch to time race teams
    stopwatch = turtle.Turtle()
    stopwatch.hideturtle()

    # Declare timers list 
    TIMERS = [float()] * len(TEAMS)

    # Outer Race Loop (for each Team)
    for i, t in enumerate(TEAMS):
        #Initialize runners and reset the stopwatch
        trtl_height = 1.0
        trtl_width = 1.0
        pen_size = 1
        stopwatch.clear()
        # Start the stopwatch for the team currently running
        start = time.time()

        # Inner Race Loop (to draw the turtle racers running)
        for runner in range (0, 4):
            # Assign random speed to each turtle runner
            trtl_speed  = random.randint(1,10) / 5
                    
            # Set the pen size and runner speed
            t.shapesize(trtl_width,trtl_height, 1) 
            t.pensize(pen_size)
            t.speed(trtl_speed)
            
            # Run the turtle
            t.forward(WIDTH_RELAY)

            # Increase turtle size and pen size for each runner.
            trtl_width = trtl_width + 0.25
            trtl_height = trtl_height + 0.25
            pen_size = pen_size + 2
            # End Inner Race Loop

        # Capture the timer for the team.
        TIMERS[i] = "%0.3f" %(time.time() - start)
        # End Outer Race Loop

    return TIMERS


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Wrap up & show winner function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display_results(times_taken):
    """
    Display results and winner.
    @authors: Matt
    """
    #Declare variables    
    lowest_time = float() 
    lowest = str()
    winner = lowest
    t = turtle.Turtle()
    #Label times 
    for i in range(0,len(times_taken)):        
        t.goto(TRACK_END_X + PADDING_LANE_LABEL, lane_n_center_y_pos(i))
        t.write(times_taken[i])
    #Loop to find the lowest time
    for x in range(0,len(times_taken)):
        if times_taken[x] < lowest_time:
            lowest_time = times_taken[x]      
    #If statement that prints winner and time to the screen
    if winner == NAMES_ALLOWED[0]:
        print(NAMES_ALLOWED[0])
        print(lowest_time)
    elif winner == NAMES_ALLOWED[1]:
        print(NAMES_ALLOWED[1])
        print(lowest_time)
    elif winner == NAMES_ALLOWED[2]:
        print(NAMES_ALLOWED[2])
        print(lowest_time)
    elif winner == NAMES_ALLOWED[3]:
        print(NAMES_ALLOWED[3])
        print(lowest_time)
    elif winner == NAMES_ALLOWED[4]:
        print(NAMES_ALLOWED[4])
        print(lowest_time)
    elif winner == NAMES_ALLOWED[5]:
        print(NAMES_ALLOWED[5])
        print(lowest_time)     

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """
    Main function to run the turtle relay race.
    @authors: Kevin
    """
    # get input (number of teams) from user
    n_teams = get_input_for_number_of_teams()

    # set up the screen
    # set_scenery(n_teams=n_teams)

    # TODO: Build teams list; assign id, color, name, speeds; allocate time (Matt?)
    # teams = [build_team(i) for i in range(n_teams)]
    # turtles = [create_turtle(color, speed) for color, speed in zip(COLORS_ALLOWED, SPEEDS_ALLOWED)]
    # turtles = turtles[:n_teams]
    turtles = []
    for i in range(n_teams):
        turtles.append(
            create_turtle(COLORS_ALLOWED[i])
        )
    # Set starting positions
    # TODO: use lane_n_center_y_pos() to center each team's turtle & start race (James)
    for i, t in enumerate(turtles):
        t.penup()
        t.goto(TRACK_START_X, lane_n_center_y_pos(i))
        t.pendown()

    # Race loop
    times_taken = run_race(turtles)

    # display results and winner
    display_results(times_taken)
   
    # finish program
    turtle.done()
    return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Call main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    sys.exit(main())
