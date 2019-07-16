#! /bin/python
import sys
import os
import platform
from random import shuffle
from copy import deepcopy
import subprocess as sp


def read_data(file_name, player_list):
    with open(file_name) as player_file:
        for line in player_file:
            player_list.append(line[:-1])


def main():
    file_name = ""
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = "players.txt"

    player_names = []
    read_data(file_name, player_names)
    circle = deepcopy(player_names)
    shuffle(circle)
    print(circle)

    players_string = ""
    for player in player_names[:-1]:
        players_string += player+", "

    players_string += player_names[-1]
    done = False
    while not done:
        # Clears the screen
        if platform.system() == "Linux":
            sp.call('clear', shell=True)
        elif platform.system() == "Windows":
            os.system("CLS")
        else:
            sp.call('cls', shell=True)

        print("Please Type in a name for player for whom you want the target.")
        print("Valid Players: " + players_string)
        name = input()
        if name == "quit":
            break
        if name in circle:
            index = circle.index(name)
            if index < len(circle) - 1:
                print("Target is: " + circle[index+1])
            else:
                print("Target is: " + circle[0])
        else:
            print("Not a valid name. Please choose a name in following")
            print(players_string)
        input("Press enter to continue")


if __name__ == "__main__":
    main()
