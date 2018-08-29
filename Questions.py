from termcolor import colored
import Answers
import Optio


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
    elif if_Answer == 3: #TEST
        Answers.Answer3()


################################ > STORY ADVANCING QUESTIONS FOR PLAYERS TO ANSWER < ###################################


def Question1():
    question1 = ["Decisions decisions",
                 "You do X",
                 "You just do it"]
    for_decision(question1, 1)


def Question2():
    question2 = ["You decide on that",
                 "You decide on this "]
    for_decision(question2, 2)

def Question3():
    question3 = ["Decision 1",
                 "Decision 2"]
    for_decision(question3, 3)











