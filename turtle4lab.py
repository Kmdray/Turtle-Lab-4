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


class Team:
    """
    Team class to store team information.
    @authors: Shane
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(
        self,
        _id: int,
        name: str,
        color: tuple[int, int, int],
        speeds: tuple[float, float, float, float],
    ) -> None:
        self.id = _id
        self.name = name
        self.laps_completed = int()
        self.distance_covered = float()
        self.color = color
        self.speeds = speeds

        # TODO: assign turtle to team at creation (Kevin)
        self.turtle: turtle.Turtle | None = None
        self.win_time: float = float()

    def __str__(self) -> str:
        return (
            f"Team("
            f"id={self.id},"
            f" speeds={[round(x, 2) for x in self.speeds]},"
            f" laps_completed={self.laps_completed},"
            f" distance_covered={self.distance_covered},"
            f" color={self.color},"
            f" name={self.name}"
            ")"
        )

    def starting_position(self) -> tuple[float, float]:
        """
        Returns the starting position of the team.
        @authors: Shane
        """
        return -WIDTH / 2 + PADDING_LEFT, lane_n_center_y_pos(self.id)

    def set_turtle(self, _turtle: turtle.Turtle) -> None:
        """
        Assigns a turtle to a given team.
        @authors: Shane
        """
        self.turtle = _turtle

    def victory_dance(self) -> None:
        """
        Performs a victory dance and displays win time and average speed.
        @authors:
        """
        # self.win_time = ...

    # def finish_time():
    #     # physically/mathematically calculate time to finish
    #     RELAY_LENGTH = TRACK_LENGTH / N_RELAYS
    #     total_time = float()
    #     for i in range(4):
    #         # time = distance / speed
    #         total_time += RELAY_LENGTH / self.speeds[i]
    #
    #     # or use time.time()
    #     time.time()
    #     # add change to accumulator


def get_input() -> int:
    """
    Gets number of teams and colors from user.
    Returns list of Team objects.

    @authors: Shane
    """

    # Get number of teams
    if os.environ.get("N_TEAMS"):
        n_teams = int(os.environ["N_TEAMS"])
    else:
        n_teams = int(input("Enter number of teams, between 2 and 6: "))
    if n_teams < 2 or n_teams > 6:
        raise ValueError("Number of teams must be between 2 and 6.")

    return n_teams


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

FONT_SIZE_LANE_LABELS = 12
PADDING_LANE_LABEL = 20


def lane_n_center_y_pos(n: int) -> float:
    """
    Returns the y-coordinate of the center of the nth lane.
    NOTE: starts at 1.
    @authors: Shane
    """
    return -HEIGHT / 2 + PADDING_BOTTOM + HEIGHT_LANE / 2 + (n - 1) * HEIGHT_LANE


def set_scenery(n_teams: int) -> None:
    """
    Sets up the racetrack and finish line.
    @authors: Shane
    """
    turtle.setup(width=WIDTH, height=HEIGHT)
    turtle.bgcolor("yellow")
    turtle.title("Turtle Relay Race")

    # Draw rectangular racetrack perimeter
    turtle.penup()
    turtle.goto(-WIDTH / 2 + PADDING_LEFT, -HEIGHT / 2 + PADDING_BOTTOM)
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
            -WIDTH / 2 + PADDING_LEFT + i * WIDTH_TRACK / N_RELAYS,
            -HEIGHT / 2 + PADDING_BOTTOM,
        )
        turtle.pendown()
        turtle.goto(
            -WIDTH / 2 + PADDING_LEFT + i * WIDTH_TRACK / N_RELAYS,
            HEIGHT / 2 - PADDING_TOP,
        )

    # Label lane numbers with team index
    turtle.color("black")
    for i in range(1, n_teams + 1):
        turtle.penup()
        turtle.goto(
            -WIDTH / 2 + PADDING_LANE_LABEL,
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
            -WIDTH / 2 + PADDING_LEFT,
            -HEIGHT / 2 + PADDING_BOTTOM + i * HEIGHT_LANE,
        )
        turtle.pendown()
        turtle.forward(WIDTH_TRACK)

    # Hide cursor
    turtle.hideturtle()


# TODO: functions to perform laps, relay exchanges, size changes (James)
# for team in teams:
#     for relay in N_RELAYS:
#         # move forward
#         # change size
#         # change color
#         pass

# functions to decide winner, terminate race, display results

colors_allowed = [
    (255, 0, 0),  # red
    (0, 255, 0),  # green
    (0, 0, 255),  # blue
    (255, 165, 0),  # orange
    (255, 255, 0),  # yellow
    (128, 0, 128),  # purple
]
names_allowed = [
    "scarlet speedsters",
    "green machines",
    "blue blazers",
    "orange ocelots",
    "yellow yaks",
    "purple panthers",
]

# Main function
def main() -> int:
    """
    Main function to run the turtle relay race.
    @authors: Kevin
    """

    # get input (number of teams) from user
    n_teams = get_input()

    # set up the screen
    set_scenery(n_teams=n_teams)

    # TODO: Build teams list; decide colors, names, and speeds (Kevin)
    teams = []

    # TODO: use Shane's n_teams value to behave accordingly, not just 4 teams
    #       as is hard-coded below (Kevin, James)
    # TODO: use Team.starting_position() to center each team (James)

    colors = ["red", "green", "blue", "orange"]
    # Speeds corresponding to colors
    speeds = [1, 2, 3, 4]

    # Create turtles with specific colors and speeds
    turtles = [create_turtle(color, speed) for color, speed in zip(colors, speeds)]

    # Set starting positions
    for i, t in enumerate(turtles):
        t.penup()
        t.goto(-350, -100 + i * 50)
        t.pendown()

    # Race loop

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

    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
