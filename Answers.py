import Story
import Questions


def Answer1():
    if Questions.answer == "1":
        Story.Story2()
    elif Questions.answer == "2":
        Story.Story3()
    elif Questions.answer == "3":
        Story.Story4()
    else:
        Questions.Decision(1)


def Answer2():
    if Questions.answer == "1":
        Story.Story7()
    elif Questions.answer == "2":
        Story.Story8()
    else:
        Questions.Decision(2)


def Answer3():
    print("A3 Banana")






