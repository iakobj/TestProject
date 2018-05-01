import sys, os, Questions, Answers, Story
from termcolor import colored


# Prints game title in console
def GameTitle():
   Title = open("GameName.txt").read()
   print (Title)

GameTitle()


# Prints greetings text in console
def Greetings():
   os.chdir("TestScript")
   global Greetings
   Greetings = open("1Story.txt").read()
   print (Greetings)

Greetings()

Story.Initialize()











