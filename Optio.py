import sys, os, Story, Answers, Questions, Enemies, Fight
from termcolor import colored


# Optio – One per century as second-in-command to the centurion. Could also fill several other specialized roles on an ad hoc basis.


class player:

    def __init__(self, name, health, strength, defence, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.luck = luck




def playerSetup():
    name = input(colored("\n What is your name soldier? ", "yellow"))










