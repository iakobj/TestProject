import os
import Questions
import Optio


# Prints game title in console
def game_title():
    Title = open("GameName.txt").read()
    print(Title)


game_title()


# Prints greetings text in console when called in initialize()
def greetings():
    os.chdir("TestScript")
    Greetings = open("1Story.txt").read()
    print(Greetings)


# Starting the game
def Initialize():
    Optio.playerSetup()
    Optio.pointsSetup()
    greetings()
    Questions.Question1()



Initialize()











