import time
import random
import sys
import Mobs
from Mobs import enemy_template, enemy_encounter


def battle_loop(player_health, player_strength, player_agility, player_shield, enemy):
    print(f"\nA {enemy.name} has appeared!\n")
    
    while player_health > 0 and enemy.health > 0:
        print(f"Your Health: {player_health}")
        print(f"{enemy.name} Health: {enemy.health}")
        
        action = input("Choose an action - Attack (a), Defend (d), or Dodge (o): ").strip().lower()
        
        if action == "a":
            damage = player_strength + random.randint(0, 5)
            enemy.health -= damage
            print(f"\nYou attack the {enemy.name} for {damage} damage!\n")

        elif action == "d":
            blocked_damage = player_shield + random.randint(1, 3)    
            print(f"\nYou brace yourself, preparing to absorb {blocked_damage} damage.\n")

        elif action == "o":
            dodge_chance = min(90, player_agility * 10)
            if random.randint(1, 100) <= dodge_chance:
                print(f"\nYou swiftly dodge the {enemy.name}'s attack!\n")
                continue
            else:
                print("\nYou failed to dodge!\n")

        if enemy.health > 0:
            enemy_damage = enemy.attack - (blocked_damage if action == "d" else 0)
            enemy_damage = max(0, enemy_damage)
            player_health -= enemy_damage
            print(f"The {enemy.name} strikes back, dealing {enemy_damage} damage!\n")

        time.sleep(1.5)

    if player_health <= 0:
        print("\nYou have been defeated...\n")
    else:
        print(f"\nYou have defeated the {enemy.name}!\n")

    return player_health  


def typing_animation(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def spawn_enemy(player_health, player_strength, player_agility, player_shield):
    enemy = enemy_encounter()
    return battle_loop(player_health, player_strength, player_agility, player_shield, enemy)


username = ""
health = 0
strength = 0
agility = 0
luck = 0
shield = 0
playerDead = False

enemy_encounter()

print("Welcome to *game title*, we hope you enjoy!")
time.sleep(0.5)
username = input("Enter the Player's name: ")
time.sleep(0.5)
print(f"Welcome {username}! You may now choose your stats.")
time.sleep(0.5)

playerCheating = True
while playerCheating:
    health = int(input("Health points (Each point = +5 Health): ")) * 5
    strength = int(input("Strength points (Each point = +5 Strength): ")) * 5
    agility = int(input("Agility points (Each point = +1 Agility): "))
    shield = int(input("Shield points (Each point = +1 Shield): "))
    luck = int(input("Luck points (Each point = +1 Luck): "))

    playerstats = [health // 5, strength // 5, agility, shield, luck]
    if sum(playerstats) != 6:
        print("Total stat points must equal 6. Try again.")
    else:
        playerCheating = False

print(f"Stats confirmed: Health = {health}, Strength = {strength}, Agility = {agility}, Shield = {shield}, Luck = {luck}")

gameMode = ""
while gameMode not in ["hard", "medium", "easy"]:
    gameMode = input("Choose mode: Hard, Medium, Easy: ").strip().lower()

print("The year is 2245...")
time.sleep(2)

if gameMode == "easy":
    print("You begin in a bustling city on Mars...")
    time.sleep(2)
    typing_animation("Traveling....", delay=0.1)

    print("You arrive at the moon. It looks eerie...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)
    
    print("After a hard-fought battle, you hear clicking noises...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)
    
    print("You press forward, deeper into the station...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("The fight leaves you shaken, but alarms begin blaring...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("Something big is coming...")
    time.sleep(2)

elif gameMode == "medium":
    print("Your mission begins on a derelict space station...")
    time.sleep(2)
    typing_animation("Docking....", delay=0.1)

    print("The hangar is eerily silent...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("Flickering lights reveal movement in the corridors...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("You find signs of a struggle...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("Emergency systems activate...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("The ground beneath you trembles...")
    time.sleep(2)

elif gameMode == "hard":
    print("A distress signal leads you to a drifting starship...")
    time.sleep(2)
    typing_animation("Approaching....", delay=0.1)

    print("You step into total darkness...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("Organic growths pulse faintly as if alive...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("The temperature drops, ice forming on the walls...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("Emergency lights flicker to life, revealing horror...")
    time.sleep(2)
    health = spawn_enemy(health, strength, agility, shield)

    print("A deep voice booms: 'You cannot escape.'")
    time.sleep(2)

print("Tough luck, rerun the code to play again!")
