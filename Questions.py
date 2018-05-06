import sys, os, Answers, Story
from termcolor import colored


# Prints questions about story progress for players to answer
def for_decision(A_list, IF_Answer):
    decision = 1
    for i in A_list:
        print(colored(decision, "cyan"), colored(i, "magenta"))
        decision = decision + 1
    Decision(IF_Answer)


# Setting the default answer to 0
answer = "0"

# Asking the player for decision relevant to story progress
def Decision(if_Answer):
    global answer
    answer = input(colored("\n What are you going to do? ", "yellow"))

    # Calling the right if statement relevant to the question
    if if_Answer == 1:
        Answers.Answer1()
    elif if_Answer == 2:
        Answers.Answer2()



################################ > STORY ADVANCING QUESTIONS FOR PLAYERS TO ANSWER < ###################################



def Question1():
    question1 = ["You join your drinking buddies",
                 "You join pretty ladies",
                 "You just dance"]

    for_decision(question1, 1)


def Question2():
    question2 = ["You run back to your station to go check out if the moving is still there",
                 "You go to sleep"]

    for_decision(question2, 2)









