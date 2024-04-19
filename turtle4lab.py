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


def create_turtle(color, speed):
    """
    Function to create a turtle with specific color and speed.
    @authors: Kevin
    """
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.speed(speed)
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
def run_race(n_teams):
    # Local variables
    speed = int()
    one_time = float()
    trtl_height = float()
    trtl_width = float()
    
    # Create Timer
    timer_text = turtle.Turtle()
    timer_text.hideturtle()
    

    # Declare teams and timers lists 
    teams = [""] * n_teams
    timers = [""] * len(teams)

##################################################################    
##    # Load teams list for correct number of teams
##    for i in range (0, n_teams):
##        teams[i] = turtles[i]
##        print(locals())
    
##    # Set starting positions
##    for i, t in enumerate(teams):
##        t.speed(7)
##        t.penup()
##        t.goto(TRACK_START_X, lane_n_center_y_pos(i))
##        t.pendown()
########################################################################

    # Create runners and Set starting positions
    for team in range(0, len(teams)):
        t = turtle.Turtle()
        t.shape('turtle')
        t.color(COLORS_ALLOWED[team])
        t.speed(7)
        t.penup()
        t.goto(TRACK_START_X, lane_n_center_y_pos(team))
        t.pendown()
        
        #Initialize turtle and time
        trtl_height = 0.5
        trtl_width = 0.5
        pen_size = 1
        timer_text.clear()

        # Start the timer for the team currently running
        start = time.time()
        
        # Inner Race Loop (to draw the racers running)
        for lap in range (0, 4):
            speed  = random.randint(1,10) / 5
            # Increases turtle size on each lap.
            trtl_width = trtl_width + 0.25
            trtl_height = trtl_height + 0.25
                    
            #set the pen size and runner speed
            t.shapesize(trtl_width,trtl_height, 1) 
            t.pensize(pen_size)
            t.speed(speed)
            
            # Run the turtle
            t.forward(WIDTH_RELAY)

            # Increase pen size for each runner.
            pen_size = pen_size + 2
            #end Inner Race Loop

        #Capture and display the timer for the team.
        one_time = "%0.3f" %(time.time() - start)
        timers[team] = one_time
##        timer_text.write("Time: " + "%0.2f" %(time.time() - start),align="center", font=("Courier", 30,))
        #End Outer Race Loop

    return timers


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Wrap up & show winner function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display_results():
    """
    Display results and winner.
    @authors: Matt
    """


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """
    Main function to run the turtle relay race.
    @authors: Kevin
    """
    # CALLING OTHER FUNCTIONS??? - Not sure exactly how to call these and where. Will discuss in our meeting.
    # get_input_for_number_of_teams() #Call - get input
    # turtle.reset #??  #Reset???
    # set_scenery(n_teams: int) #Call - set scenery
    # lane_n_center_y_pos(n: int) #Call - lane n center
    # create_turtle(color: str, speed: float) #Call - create turtle
    # move_forward(t: turtle.Turtle) #Call - move forward

    # get input (number of teams) from user
    n_teams = get_input_for_number_of_teams()

    # set up the screen
    set_scenery(n_teams=n_teams)

    # TODO: Build teams list; assign id, color, name, speeds; allocate time (Matt?)
    # teams = [build_team(i) for i in range(n_teams)]

    # TODO: use Shane's n_teams value to behave accordingly, not just 4 teams
    #       as is hard-coded below (Kevin, James)
    # TODO: use COLORS_ALLOWED/NAMES_ALLOWED to generate all 6 (Kevin, James, Matt)
    # Create turtles with specific colors and speeds
    turtles = [create_turtle(color, speed) for color, speed in zip(COLORS_ALLOWED, SPEEDS_ALLOWED)]

    # Set starting positions
    # TODO: use lane_n_center_y_pos() to center each team's turtle & start race (James)
    for i, t in enumerate(turtles):
        t.penup()
        t.goto(TRACK_START_X, lane_n_center_y_pos(i))
        t.pendown()

    # Race loop
    run_race(n_teams)

    # display results and winner
    display_results()

    # finish program
    turtle.done()
    return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Call main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    sys.exit(main())
