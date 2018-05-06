import os
import Questions
import Optio

# Prints game title in console
def GameTitle():
   Title = open("GameName.txt").read()
   print (Title)

# Prints greetings text in console
def Greetings():
   os.chdir("TestScript")
   Greetings = open("1Story.txt").read()
   print (Greetings)

# Starting the game
def Initialize():
    Optio.playerSetup()
    Greetings()
    Questions.Question1()

GameTitle()

Initialize()











