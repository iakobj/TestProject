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


    def printPlayerInfo(self):
        print(self.name)
        print(self.health)
        print(self.strength)
        print(self.defence)
        print(self.luck)


def playerSetup():
    optio = Player

    name = input(colored("\n What is your name soldier? ", "yellow"))
    optio.name = name
    print("\n Hello there soldier " + optio.name)

    health = input("\n Type in your Health: ")
    optio.health = health

    strength = input("\n Type in your Strength: ")
    optio.strength = strength

    defence = input("\n Type in your Defence: ")
    optio.defence = defence

    luck = input("\n Type in your Luck: ")
    optio.luck = luck

    Player.printPlayerInfo(optio) #calling for test purposes










