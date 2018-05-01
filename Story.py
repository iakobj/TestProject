import sys, os, Answers, Questions
from termcolor import colored

def Initialize():
    Questions.Question1()

def Story2():
   Story = open("2Story.txt").read()
   print (Story)
   Answers.Decision()


def Story3():
    Story = open("3Story.txt").read()
    print(Story)
    Questions.Question2()
    Answers.Decision()

def Story4():
    Story = open("4Story.txt").read()
    print(Story)
    Answers.Decision()




