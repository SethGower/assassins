#! /bin/python
import os
import platform
import subprocess as sp
import sys
from copy import deepcopy
from random import shuffle


def clear_screen():
    if platform.system() == "Linux":
        sp.call('clear', shell=True)
    elif platform.system() == "Windows":
        os.system("CLS")
    else:
        sp.call('cls', shell=True)


class Circle(object):
    def __init__(self, player_list):
        self.player_list = player_list
        self.shuffled_list = deepcopy(player_list)
        shuffle(self.shuffled_list)

        self.players_string = ""
        for player in self.player_list[:-1]:
            self.players_string += player+", "
        self.players_string += player_list[-1]

        matches = {}
        for i in range(len(player_list)-1):
            matches[self.shuffled_list[i]] = self.shuffled_list[i+1]
        matches[self.shuffled_list[-1]] = self.shuffled_list[0]
        self.matches = matches

    def get_target(self, name):
        if name in self.matches.keys():
            return self.matches[name]
        else:
            return None

    def __repr__(self):
        result = ""
        for player in self.shuffled_list[:-1]:
            result += player + ", "
        result += self.shuffled_list[-1]
        return "Circle: " + result


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

    circle = Circle(player_names)

    done = False
    while not done:
        # Clears the screen
        clear_screen()
        print("Please Type in a name for player for whom you want the target.")
        print("Valid Players: " + circle.players_string)
        name = input()
        if name == "quit":
            break
        target = circle.get_target(name)
        if target is not None:
            print("Target is {}".format(target))
        else:
            print("Not a valid name. Please choose a name in following")
            print(circle.players_string)
        input("Press enter to continue")


if __name__ == "__main__":
    main()
