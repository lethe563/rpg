import action
import equipment
import enviroment
import json
import random

def main():
    current_x = 0
    current_y = 0
    health = 100.0 #User's health
    attack = 10 #User's attack strength
    first_time = True
    continue_quest = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive
        current_x, current_y, continue_quest = action.next_step(first_time, current_x, current_y)
        first_time = False
        if continue_quest == False:
            break
        enviroment.generator(current_x, current_y)
        room_number, room_size, room_material, enemy_name, enemy_health, enemy_attack = enviroment.current_room(current_x, current_y)
        #print("x = " + str(current_x) + " y = " + str(current_y) + "\nEnemy:\t\t" + enemy_name + "\t\tYou:\nHealth\t\t" + str(enemy_health) + "\t\t\t" + str(health) +"\nAttack rating\t" + str(enemy_attack) + "\t\t" + str(attack))
        print("You are in a " + room_size + " " + room_material + " room.\nYou're facing a: " + enemy_name + "\nEnemy health: " + str(enemy_health) + "\nEnemy attack rating: " + str(enemy_attack))#Description of room
        health = action.combat(health, attack, enemy_name, enemy_health, enemy_attack, room_number) #Begin combat. We only need health variable back.
        dead = action.death(health)



main()
