import Story, Questions
from termcolor import colored





def Answer1():

    if Questions.Answer == "1":
        Story.Story2()

    elif Questions.Answer == "2":
        Story.Story3()

    elif Questions.Answer == "3":
        Story.Story4()

    else:
        Questions.Decision(1)

def Answer2():

    if Questions.Answer == "1":
        Story.Story2()

    elif Questions.Answer == "2":
        Story.Story3()

    else:
        Questions.Decision(2)






