from termcolor import colored

# Optio – One per century as second-in-command to the centurion
# Could also fill several other specialized roles on an ad hoc basis.


class Player:
    def __init__(self, name, health, strength, defence, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.luck = luck
        #self.points = points


    def printPlayerInfo(self):
        print("\nName: ", self.name)
        print("Health: ", self.health)
        print("Strength: ", self.strength)
        print("Defence: ", self.defence)
        print("Luck: ", self.luck)
        print("\n")
        #print(self.points)


def playerSetup():
    optio = Player

    name = input(colored("\nWhat is your name soldier? ", "yellow"))
    optio.name = name

    print("\nHello there soldier " + optio.name + " Welcome to the game.\n")


def pointsSetup():

    optio = Player
    optio.health = 0
    optio.strength = 0
    optio.defence = 0
    optio.luck = 0

    global points
    points = 200

    print(optio.name, "Here you can declare points to your character \n")

    print("Points remaining: ", points)


    while points > 0:   #FIX THE IF STATEMENTS AND THIS WHILE STUFF

        health = int(input("\nType in your Health: "))
        if points > -1:
            optio.health =  health + optio.health
            points = points - optio.health
            print("Points remaining: ", points)

        strength = int(input("\nType in your Strength: "))
        if points > -1:
            optio.strength = optio.strength + strength
            points = points - optio.strength
            print("Points remaining: ", points)

        defence = int(input("\nType in your Defence: "))
        if points > -1:
            optio.defence = optio.defence + defence
            points = points - optio.defence
            print("Points remaining: ", points)

        luck = int(input("\nType in your Luck: "))
        if points > -1:
            optio.luck = optio.luck + luck
            points = points - optio.luck
            print("Points remaining: ", points)

        Player.printPlayerInfo(optio) #calling for test purposes










