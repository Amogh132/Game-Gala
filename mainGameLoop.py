import time
import random
import Mobs
import playerClass


username = ""
health = 0
strength = 0
agility = 0
luck = 0
shield = 0
playerCheating = True
playerDead = False
playerClass = ""
choosingPlayerClass = 0




#put sum welcome stuff here
while playerCheating == True:
    print("Welcome to the *game title* we hope you enjoy!")
    time.sleep(0.5)
    username = input("Enter in the Player's name: ")
    time.sleep(0.5)
    print("Welcome" + " " + username + " " + "You may now choose your stats, keep in mind that you only have 6 stat points, choose your stats wisely!")
    time.sleep(0.5)
    health = int(input("How many points would you like to put inside Heath? Health increases in increaments of 5."))
    time.sleep(0.5)
    strength = int(input("How many points would you like to put inside Strenght? Strength increases in increments 1."))
    time.sleep(0.5)
    agility = int(input("How many points would you like to put inside Agility? Agility increases in increments 1."))  
    time.sleep(0.5)   
    shield = int(input("How many points would you like to put inside Shield? Shield increases in increments of 1."))    
    time.sleep(0.5)
    luck = int(input("How many points would you like to put inside Luck? Luck increases in increaments of 1."))    
    playerstats = [health, strength, agility, shield, luck]

    if sum(playerstats) > 6:
        print("Please reenter stats.")
    else:
        playerstats[1] = playerstats[1] * 5
        playerCheating = False

#updating player stats based on what they chose
for i in range(len(playerstats)):
    if playerstats[i] > choosingPlayerClass:
        choosingPlayerClass == i

if choosingPlayerClass == 1:
    playerClass = playerClass.giant.className

print(playerClass)