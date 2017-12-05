import action
import equipment
import enviroment
import json
import random

def combat(health, attack, enemy_name, enemy_health, enemy_attack):
    #print("Enemy name: " + enemy_name + "\nEnemy health: " + str(enemy_health) + "\nCurrent health : " + str(health))
    while health > 0 and enemy_health > 0:
        command = input("Do you wish to attack? (y/n)d")
        if command == "y":
            enemy_health -= attack * random.random() #Damage inflicted on enemy is your attack rating times a random number between 0 and 1
            health -= enemy_attack * random.random() #Damage inflicted on you is your enemy's attack rating times a random number between 0 and 1
            print("Success!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "n":
            health -= enemy_attack
            print("Failure! Just press y next time!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "d": #Die for testing
            break
        else:
            print("Please enter either y or n.")

    return(health)

def next_step(first_time):
    decision = False #Decision to continue on quest
    while decision == False: #Continue loop until a decision is reached
        if first_time == True:
            quest = input("Would you like to start your quest? y/n/e") #i is for inventory testing. e is for equip testing
        else:
            quest = input("Would you like to continue your quest? y/n/e") #i is for inventory testing

        if quest == "y": #Continue game
            decision = True #Break the while decision loop
            room = enviroment.rooms()
            baddie = enviroment.baddies()
        elif quest == "n": #End game
            decision = True #To break the while decision loop
            room = "quit"
            baddie = "quit"
            print("Goodbye!")
        elif quest == "e":
            equipment.change_equipment()
        else:
            print("Please enter either y or n.")
            decision = False #Go through the while decision loop again

    return room, baddie

def death(health):
    dead = True
    if health <= 0:
        dead = True
        print("You are dead")
    else:
        dead = False
    return dead
