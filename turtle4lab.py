#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:46:15 2024 -0400

Title: Turtle Relay Race

Description:    This program simulates a relay race between multiple teams using the
                turtle module.

@authors: Kevin, Shane, James, Matt
"""
import os
import random
import sys
import turtle


class Team:
    """
    Team class to store team information.
    @authors: Shane
    """

    def __init__(
        self,
        id: int,
        name: str,
        color: tuple[int, int, int],
        speeds: tuple[float, float, float, float],
        # turtle: turtle.Turtle,
    ) -> None:
        self.id = id
        self.name = name
        self.color = color
        self.speeds = speeds
        # TODO: fill this in if we're using time.time() (James)
        # self.start_time = ...

        # TODO: assign turtle to team at creation (Kevin)
        # self.turtle = turtle
        self.race_time: float = float()
        self.relay_exchanges_completed = int()
        # self.distance_covered = float()

    def __str__(self) -> str:
        """Shows details for the team"""
        return (
            f"Team("
            f"id={self.id},"
            f" speeds={[round(x, 2) for x in self.speeds]},"
            f" color={self.color},"
            f" name={self.name}"
            ")"
        )

    def starting_position(self) -> tuple[float, float]:
        """
        Returns the starting (x, y) position of the team at the start of the racetrack.
        @authors: Shane
        """
        return TRACK_START_X, lane_n_center_y_pos(self.id)

    def victory_dance(self) -> None:
        """
        Performs a victory dance and displays win time and average speed.
        @authors: Matt?
        """
        # self.win_time = ...

    # def finish_time(t2):
    #     # physically/mathematically calculate time to finish
    #     RELAY_LENGTH = TRACK_LENGTH / N_RELAYS
    #     total_time = float()
    #     for i in range(4):
    #         # time = distance / speed
    #         total_time += RELAY_LENGTH / self.speeds[i]
    #
    #     # or use time.time() to track elapsed time
    #     t1 = time.time()
    #     # do relay


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
TRACK_START_Y = -HEIGHT / 2 + PADDING_BOTTOM

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Input & setup functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_scenery(n_teams: int) -> None:
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
    for i in range(1, N_RELAYS):  # 3 lines make 4 relay zones
        turtle.penup()
        turtle.goto(
            TRACK_START_X + i * WIDTH_RELAY,
            TRACK_START_Y,
        )
        turtle.pendown()
        turtle.goto(
            TRACK_START_X + i * WIDTH_RELAY,
            HEIGHT / 2 - PADDING_TOP,
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
    for i in range(1, N_LANES):  # 5 lines make 6 lanes
        turtle.penup()
        turtle.goto(
            TRACK_START_X,
            TRACK_START_Y + i * HEIGHT_LANE,
        )
        turtle.pendown()
        turtle.forward(WIDTH_TRACK)

    # Hide cursor
    turtle.hideturtle()


def get_input_for_number_of_teams() -> int:
    """
    Gets number of teams from user input.
    @authors: Shane
    """
    # Get number of teams
    if os.environ.get("N_TEAMS"):
        n_teams = int(os.environ["N_TEAMS"])
    else:
        n_teams = int(input("Enter number of teams, between 2 and 6: "))

    # Verify it's between two and six
    if n_teams < 2 or n_teams > 6:
        raise ValueError("Number of teams must be between 2 and 6.")

    return n_teams


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Race/relay functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TODO: functions to perform laps, relay exchanges, size changes (James, Matt)
# for team in teams:
#     for relay in N_RELAYS:
#         # move forward
#         # change size
#         # change color
#         pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Wrap up & show winner functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TODO: functions to decide winner, terminate race, display results (Matt)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def lane_n_center_y_pos(n: int) -> float:
    """
    Returns the y-coordinate of the center of the nth lane. NOTE: starts at 0.
    @authors: Shane
    """
    return TRACK_START_Y + HEIGHT_LANE / 2 + n * HEIGHT_LANE


def create_turtle(color: str, speed: float) -> turtle.Turtle:
    """
    Function to create a turtle with specific color and speed.
    @authors: Kevin
    """
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.speed(speed)
    return t


def move_forward(t: turtle.Turtle) -> None:
    """
    Function to move the turtle forward by 100 units.
    @authors: Kevin
    """
    t.forward(100)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main() -> int:
    """
    Main function to run the turtle relay race.
    @authors: Kevin
    """

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
        t.goto(-350, -100 + i * 75)
        t.pendown()

    # Race loop
    # TODO: expand this functionality/track time to finish/co-ordinate functions (Kevin)
    # for team in teams:
    #     team.turtle(...)
    #     team.finish_time = now()

    laps = 4
    for lap in range(1, laps + 1):
        print(f"Lap {lap}:")
        for t in turtles:
            move_forward(t)
            if t.xcor() >= 350:
                # Change turtle color and reset position
                t.color(random.choice(colors))
                t.speed(speeds[colors.index(t.color())])  # type: ignore
                # TODO: use new function to get Y-position: lane_n_center_y_pos(n: int)
                t.goto(-350, -100 + colors.index(t.color()) * 50)  # type: ignore

    # finish program
    turtle.done()
    return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Call main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    sys.exit(main())
