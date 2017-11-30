import json
import random

def combat(health, enemy_health, attack, enemy_attack):
    print("Enemy health: " + str(enemy_health))
    while health > 0 and enemy_health > 0:

        command = input("Do you wish to attack? (y/n)")
        if command == "y":
            enemy_health -= attack
            health -= enemy_attack
            print("Success!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "n":
            health -= enemy_attack
            print("Failure! Just press y next time.\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        else:
            print("Please enter either y or n")

    return(health)

def baddies():

    baddies_file = open("baddies.txt", "r")
    baddies_list = json.loads(baddies_file.read())
    baddie = random.choice(list(baddies_list))
    return baddie

def main():
    health = 100 #User's health
    enemy_health = 100
    attack = 10
    enemy_attack = 5
    dead = False #If the user is dead, change to True
    while dead == False:

        health = combat(health, enemy_health, attack, enemy_attack)
        if health <= 0:
            dead = True



    print("You are dead.")
main()
