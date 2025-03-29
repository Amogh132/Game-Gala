import time
import random

usermame = ""
health = 0
strength = 0
agility = 0
luck = 0
shield = 0

def userDetails(username, health, strength, agility, luck, shield):
    #put sum welcome stuff here
    
    username = input("Enter in the Player's name: ")
    time.sleep(2)
    print("Welcome" + " " + username + " " + "You may now choose your stats, keep in mind that you only have 5 stat points, choose your stats wisely!")
    time.sleep(2)
    health = int(input("How many points would you like to put inside Heath? Health increases in increaments of 5."))
    time.sleep(2)
    strength = int(input("How many points would you like to put inside Strenght? Strength increases in increments 1."))
    time.sleep(2)
    agility = int(input("How many points would you like to put inside Agility? Agility increases in increments 1."))  
    time.sleep(2)   
    shield = int(input("How many points would you like to put inside Shield? Shield increases in increments of 1."))    
    time.sleep(2)
    luck = int(input("How many points would you like to put inside Luck? Luck increases in increaments of 1."))    
    playerstats = [health, strength, agility, shield, luck]

    if sum(playerstats) > 5:
        print("Nice try cheating lil bro, rerun the code.") #we are gonna change this later
    else:
        playerstats[1] = playerstats[1] * 5




