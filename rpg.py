import json
import random

def combat(health, attack, enemy_name, enemy_health, enemy_attack):
    print("Enemy name: " + enemy_name + "\nEnemy health: " + str(enemy_health))
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

    baddies_file = open("baddies.txt", "r") #Open file with list of enemies.
    baddies_list = json.loads(baddies_file.read()) #Pulling list of enemies and arranging as json.
    random_baddie = random.choice(list(baddies_list)) #Pulling a random enemy name from the list.
    baddie = baddies_list[random_baddie] #Pulling the dictonary for the enemy, by using the name generated in random_baddie line, as a key.
    return baddie

def main():
    health = 100 #User's health
    attack = 10 #User's attack strength

    dead = False #If the user is dead, change to True
    while dead == False:
        enemy = baddies() #Generating random enemy from baddies()
        enemy_name = enemy["name"]
        enemy_health = int(enemy["health"])
        enemy_attack = int(enemy["attack"])
        health = combat(health, attack, enemy_name, enemy_health, enemy_attack)
        if health <= 0:
            dead = True


    print("You are dead.")
main()
