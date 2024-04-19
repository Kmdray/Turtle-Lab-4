import turtle
import os
import random

# Function to get input and generate teams
def get_input() -> list[team]:
    colors_allowed = [
        (255, 0, 0),   # red
        (0, 255, 0),   # green
        (0, 0, 255),   # blue
        (255, 165, 0), # orange
        (255, 255, 0), # yellow
        (128, 0, 128), # purple
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
        team = {
            "id": i,
            "color": colors_allowed[i],
            "name": names_allowed[i],
            "speeds": (
                2 + random.random(),
                3 + random.random(),
                4 + random.random(),
                5 + random.random(),
            ),
        }
        teams.append(team)

    return teams

# Main function
def main():
    # Get the list of teams
    teams = get_input()

    # Print the list of teams
    for team in teams:
        print(f"Team {team['id']}: {team['name']} (Color: {team['color']}, Speeds: {team['speeds']})")

if __name__ == "__main__":
    main()
