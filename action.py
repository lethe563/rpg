import action
import equipment
import enviroment
import json
import random

def combat(health, attack, enemy_name, enemy_health, enemy_attack, room_number):
    while health > 0 and enemy_health > 0:
        command = input("Do you wish to attack? (y/n)d")
        if command == "y":
            enemy_health -= attack * random.random() #Damage inflicted on enemy is your attack rating times a random number between 0 and 1
            health -= enemy_attack * random.random() #Damage inflicted on you is your enemy's attack rating times a random number between 0 and 1
            if enemy_health <= 0:
                print("Your enemy is defeated!")
            else:
                print("Success!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
            enviroment.change_current_room(room_number, enemy_health)
        elif command == "n":
            health -= enemy_attack
            print("Failure! Just press y next time!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
            enviroment.change_current_room(room_number, enemy_health)
        elif command == "d": #Die for testing
            break
        else:
            print("Please enter either y or n.")

    return(health)

def next_step(first_time, current_x, current_y):
    decision = False #Decision to continue on quest
    continue_quest = True
    while decision == False: #Continue loop until a decision is reached
        if first_time == True:
            quest = input("Would you like to start your quest? y/n/equip") #e is for equip testing
        else:
            quest = input("What would you like to do? /n/s/e/w/equip/q")

        if quest == "y":
            decision = True
        elif quest == "n":
            decision = True
            current_y = current_y + 1
        elif quest == "s":
            decision = True
            current_y = current_y - 1
        elif quest == "e":
            decision = True
            current_x = current_x + 1
        elif quest == "w":
            decision = True
            current_y = current_y - 1
        elif quest == "q": #End game
            decision = True #To break the while decision loop
            continue_quest = False
            print("Goodbye!")
        elif quest == "equip":
            equipment.change_equipment()
        else:
            print("Please enter either y or n.")
            decision = False #Go through the while decision loop again

    return current_x, current_y, continue_quest

def death(health):
    dead = True
    if health <= 0:
        dead = True
        print("You are dead")
    else:
        dead = False
    return dead
