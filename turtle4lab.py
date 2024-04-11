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


def set_scenery(n_teams: int) -> None:
    """
    Sets up the racetrack and finish line.
    @authors: shane
    """

    width = 800
    height = 600
    padding = 50

    turtle.setup(width=width, height=height)
    turtle.bgcolor("yellow")
    turtle.title("Turtle Relay Race")

    # Draw rectangular racetrack perimeter
    turtle.penup()
    turtle.goto(-width / 2 + padding, -height / 2 + padding)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(5)
    turtle.forward(width - 2 * padding)
    turtle.left(90)
    turtle.forward(height - 2 * padding)
    turtle.left(90)
    turtle.forward(width - 2 * padding)
    turtle.left(90)
    turtle.forward(height - 2 * padding)
    turtle.left(90)

    # Draw lanes
    turtle.pensize(1)
    for i in range(1, 6):
        turtle.penup()
        # 5 lines make 6 lanes
        turtle.goto(
            -width / 2 + padding,
            (-height / 2 + padding) + i * (2 * padding) * 5 / 6,
        )
        turtle.pendown()
        turtle.forward(width - 2 * padding)

    # Label lanes
    for i in range(1, n_teams + 1):
        turtle.penup()
        turtle.goto(
            -width / 2 + 20,
            (-250 + 500 / 6 / 2) + (i - 1) * (2 * padding) * 5 / 6 - 12,
        )
        turtle.pendown()
        turtle.write(i, font=("Arial", 12, "normal"))


# functions to perform laps, relays, size changes, etc.

# functions to decide winner, display results, etc.


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
    # input("Press enter to exit...")
    # exit()

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
                t.goto(-350, -100 + colors.index(t.color()) * 50)

    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
