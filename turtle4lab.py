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
    @authors: kevin
    """
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.speed(speed)
    return t


def move_forward(t: turtle.Turtle) -> None:
    """
    Function to move the turtle forward by 100 units.
    @authors: kevin
    """
    t.forward(100)


class Team:
    """
    Team class to store team information.
    @authors: shane
    """

    def __init__(
        self,
        _id: int,
        name: str,
        color: tuple[int, int, int],
        speeds: tuple[float, float, float, float],
    ) -> None:
        self.id = _id
        self.name = name
        self.laps_completed = 0
        self.distance_covered = 0.0
        self.color = color
        self.speeds = speeds

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
        """
        return -WIDTH / 2 + PADDING_SIDE, center_lane(self.id)


def get_input() -> list:
    """
    Gets number of teams and colors from user.
    Returns list of Team objects.

    @authors: shane
    """
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

    # Get number of teams
    if os.environ.get("N_TEAMS"):
        n_teams = int(os.environ["N_TEAMS"])
    else:
        n_teams = int(input("Enter number of teams, between 2 and 6: "))
    if n_teams < 2 or n_teams > 6:
        raise ValueError("Number of teams must be between 2 and 6.")

    # Decide team colors, names, and speeds
    teams = []
    for i in range(n_teams):
        team = Team(
            _id=i,
            color=colors_allowed[i],
            name=names_allowed[i],
            speeds=(
                2 + random.random(),
                3 + random.random(),
                4 + random.random(),
                5 + random.random(),
            ),
        )
        teams.append(team)

    return teams


# Constants
N_LANES = 6
N_RELAYS = 4

WIDTH = 800
HEIGHT = 600

PADDING_TOP = 50
PADDING_BOTTOM = 150
PADDING_SIDE = 50

HEIGHT_LANE = (HEIGHT - PADDING_TOP - PADDING_BOTTOM) / N_LANES


def center_lane(n: int) -> float:
    """
    Returns the y-coordinate of the center of the nth lane.
    NOTE: starts at 1.
    @authors: shane
    """
    return -HEIGHT / 2 + PADDING_BOTTOM + HEIGHT_LANE / 2 + (n - 1) * HEIGHT_LANE


def set_scenery(n_teams: int) -> None:
    """
    Sets up the racetrack and finish line.
    @authors: shane
    """
    turtle.setup(width=WIDTH, height=HEIGHT)
    turtle.bgcolor("yellow")
    turtle.title("Turtle Relay Race")

    # Draw rectangular racetrack perimeter
    turtle.penup()
    turtle.goto(-WIDTH / 2 + PADDING_SIDE, -HEIGHT / 2 + PADDING_BOTTOM)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(5)
    turtle.forward(WIDTH - 2 * PADDING_SIDE)
    turtle.left(90)
    turtle.forward(HEIGHT - PADDING_TOP - PADDING_BOTTOM)
    turtle.left(90)
    turtle.forward(WIDTH - 2 * PADDING_SIDE)
    turtle.left(90)
    turtle.forward(HEIGHT - PADDING_TOP - PADDING_BOTTOM)
    turtle.left(90)

    # Draw relay exchange zones
    turtle.color("red")
    turtle.pensize(1)
    for i in range(1, N_RELAYS):
        turtle.penup()
        turtle.goto(
            -WIDTH / 2 + PADDING_SIDE + i * (WIDTH - 2 * PADDING_SIDE) / N_RELAYS,
            -HEIGHT / 2 + PADDING_BOTTOM,
        )
        turtle.pendown()
        turtle.goto(
            -WIDTH / 2 + PADDING_SIDE + i * (WIDTH - 2 * PADDING_SIDE) / N_RELAYS,
            HEIGHT / 2 - PADDING_TOP,
        )

    # Label lane numbers with team index
    turtle.color("black")
    for i in range(1, n_teams + 1):
        turtle.penup()
        turtle.goto(-WIDTH / 2 + 20, -12 + center_lane(i))
        turtle.pendown()
        turtle.write(i, font=("Arial", 12, "normal"))

    # Draw lanes
    turtle.color("black")
    turtle.pensize(2)
    for i in range(1, 6):  # 5 lines make 6 lanes
        turtle.penup()
        turtle.goto(
            -WIDTH / 2 + PADDING_SIDE,
            (-HEIGHT / 2 + PADDING_BOTTOM) + i * HEIGHT_LANE,
        )
        turtle.pendown()
        turtle.forward(WIDTH - 2 * PADDING_SIDE)


# functions to perform laps, relay exchanges, size changes

# functions to decide winner, terminate race, display results


# Main function
def main() -> int:
    """
    Main function to run the turtle relay race.
    @authors: kevin
    """

    # get input (number of teams) from user
    teams = get_input()
    for team in teams:
        print(team)

    # set up the screen
    set_scenery(n_teams=len(teams))
    # turtle.done()

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
    laps = 4
    for lap in range(1, laps + 1):
        print(f"Lap {lap}:")
        for t in turtles:
            move_forward(t)
            if t.xcor() >= 350:
                # Change turtle color and reset position
                t.color(random.choice(colors))
                t.speed(speeds[colors.index(t.color())])
                # TODO: use new function to get turtle Y-position: center_lane(n: int)
                t.goto(-350, -100 + colors.index(t.color()) * 50)

    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
