import time
import random
import Enemies
import Optio



def fighting(story_no):
    print("Fighting commenced...")

    if story_no == "Story2":
        starting = False     # if player is starting is TRUE, if npc is starting is FALSE
        battle_init(starting, Enemies.Speculatores)

    elif story_no == "StoryX":
        print("You are fighting a Quaestionarius:", "\n")

    elif story_no == "StoryZ":
        print("You are fighting a Speculatores:", "\n")


def en_velites():
    print("Life:", Enemies.Velites.health)
    print("Strength:", Enemies.Velites.strength)
    print("Defence:", Enemies.Velites.defence, "\n")


def en_Quaestionarius():
    print("Life:", Enemies.Quaestionarius.health)
    print("Strength:", Enemies.Quaestionarius.strength)
    print("Defence:", Enemies.Quaestionarius.defence, "\n")


def en_Speculatores():
    print("Life:", Enemies.Speculatores.health)
    print("Strength:", Enemies.Speculatores.strength)
    print("Defence:", Enemies.Speculatores.defence, "\n")


def battle_init(starting, enemies):
    print("Battling...")
    time.sleep(2)

    if starting == True:
        player = Optio.Player    # Player
        print(player.name, "started the battle")
        battle_started(player, enemies, starting) # player - NPC
        time.sleep(1)

    elif starting == False:
        print(enemies.name, "started the battle")
        battle_started(Optio.Player, enemies, starting) # NPC - Player
        time.sleep(1)


def battle_started(player, enemies, starting):
    enemies_name = enemies.name
    player_name = player.name

    time.sleep(1)
    print("Player is:", player_name)
    time.sleep(1)
    print("Enemy is:", enemies_name)

    while player.health > 0 and enemies.health > 0:
        time.sleep(2)

        if starting == True:    # Player is dealing damage to Enemy NPC

            damageFromPlayer = ((player.strength / 100 * 40) + (player.health / 100 * 20) + (random.randint(1, player.luck)))

            enemies.defence = enemies.defence - damageFromPlayer
            print(player_name, "dealt", damageFromPlayer, "to enemy", enemies_name)
            time.sleep(1)
            print(enemies_name, "defence fell to", enemies.defence, "\n")
            time.sleep(2)

            enemies.health = enemies.health - damageFromPlayer
            print(player_name, "dealt", damageFromPlayer, "to enemy", enemies_name)
            time.sleep(2)
            print(enemies_name, "health fell to", enemies.health, "\n")
            time.sleep(2)

            if enemies.defence < 0 and enemies.health < 0:
                print("Fin")
                break

            else:
                starting = False


        elif starting == False: # Enemy NPC is dealing damage to Player

            damageFromEnemy = ((enemies.strength / 100 * (random.randint(30, 60))) + (enemies.health / 100 * 30))

            player.defence = player.defence - damageFromEnemy
            print(enemies_name, "dealt", damageFromEnemy, "to enemy", player_name)
            time.sleep(2)
            print(player_name, "defence fell to", player.defence, "\n")
            time.sleep(2)

            player.health = player.health - damageFromEnemy
            print(enemies_name, "dealt", damageFromEnemy, "to enemy", player_name)
            time.sleep(2)
            print(player_name, "health fell to", player.health, "\n")
            time.sleep(2)

            if player.defence < 0 and player.health < 0:
                print("Fin")
                break

            else:
                starting = True

    print("Fin Fin")


