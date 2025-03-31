import time
import random
import sys
import Mobs

def battle_loop(player_health, player_strength, player_agility, player_shield, enemy, current_weapon=None):
    print(f"\nA {enemy.name} has appeared!\n")
    
    if current_weapon:
        print(f"Equipped Weapon: {current_weapon.name} (+{current_weapon.damage} damage)")
    
    blocked_damage = 0
    
    while player_health > 0 and enemy.health > 0:
        print(f"\nYour Health: {player_health}")
        print(f"{enemy.name} Health: {enemy.health}")
        
        action = input("Choose an action - Attack (a), Defend (d), or Dodge (o): ").strip().lower()
        
        if action == "a":
            weapon_bonus = current_weapon.damage if current_weapon else 0
            damage = player_strength + random.randint(0, 5) + weapon_bonus
            enemy.health -= damage
            print(f"\nYou attack the {enemy.name} for {damage} damage!")

        elif action == "d":
            blocked_damage = player_shield + random.randint(1, 3)
            if current_weapon and current_weapon.name == "Energy Shield":
                blocked_damage += 2
            print(f"\nYou brace yourself, preparing to absorb {blocked_damage} damage.")

        elif action == "o":
            dodge_chance = min(90, player_agility * 10)
            if random.randint(1, 100) <= dodge_chance:
                print(f"\nYou swiftly dodge the {enemy.name}'s attack!")
                continue
            else:
                print("\nYou failed to dodge!")

        if enemy.health > 0:
            enemy_damage = enemy.attack - (blocked_damage if action == "d" else 0)
            enemy_damage = max(0, enemy_damage)
            player_health -= enemy_damage
            print(f"The {enemy.name} strikes back, dealing {enemy_damage} damage!")

        time.sleep(1.5)

    battle_result = {
        "player_health": player_health,
        "weapon_dropped": None
    }

    if player_health <= 0:
        print("\nYou have been defeated...\n")
    else:
        print(f"\nYou have defeated the {enemy.name}!\n")
        if random.random() < 0.6:
            new_weapon = Mobs.get_random_weapon()
            print(f"\nThe enemy dropped a {new_weapon}!")
            if current_weapon:
                print(f"Currently equipped: {current_weapon}")
            choice = input("Equip new weapon? (y/n): ").lower()
            if choice == 'y':
                battle_result["weapon_dropped"] = new_weapon
                print(f"You equipped the {new_weapon.name}!")
            else:
                print("You left the weapon on the ground.")

    return battle_result

def typing_animation(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spawn_enemy(player_health, player_strength, player_agility, player_shield, current_weapon, difficulty):
    if difficulty == "infinite":
        enemy = Mobs.get_infinite_enemy(player_strength)
    else:
        enemy = Mobs.enemy_encounter(difficulty)
    result = battle_loop(player_health, player_strength, player_agility, player_shield, enemy, current_weapon)
    return result["player_health"], result["weapon_dropped"]

def infinite_mode():
    current_weapon = None
    health = 150
    strength = 20
    agility = 5
    shield = 5
    level = 1
    boss_counter = 0

    print("\n=== INFINITE MODE ===")
    print("Survive as long as you can!")
    print("Every 5 levels you'll face a powerful boss!\n")
    time.sleep(2)

    while True:
        print(f"\n=== LEVEL {level} ===")
        
        # Every 5 levels = boss
        if level % 5 == 0:
            enemy = Mobs.get_boss(level)
            boss_counter += 1
        else:
            enemy = Mobs.get_infinite_enemy(level)
        
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "infinite")
        
        if health <= 0:
            print(f"\nYou survived {level} levels!")
            print(f"Defeated {boss_counter} bosses!")
            break
        
        if new_weapon:
            current_weapon = new_weapon
        
        # Progressive difficulty
        level += 1
        strength += 2
        health += 25
        agility += 1
        shield += 1

        # Special bonus every 5 levels
        if level % 5 == 0:
            print("\n⭐ Level Bonus! +50 HP and +5 ATK!")
            health += 50
            strength += 5

def story_mode(difficulty):
    username = ""
    health = 0
    strength = 0
    agility = 0
    luck = 0
    shield = 0
    current_weapon = None

    print("Welcome to SPACE ODYSSEY RPG!")
    time.sleep(0.5)
    username = input("Enter your name: ")
    time.sleep(0.5)
    print(f"\nWelcome {username}! Distribute 6 points between your stats.")
    time.sleep(0.5)

    playerCheating = True
    while playerCheating:
        print("\n--- STAT DISTRIBUTION ---")
        health = int(input("Health (1pt = +20 HP): ")) * 20
        strength = int(input("Strength (1pt = +5 ATK): ")) * 5
        agility = int(input("Agility (1pt = +1 DODGE): "))
        shield = int(input("Shield (1pt = +1 DEF): "))
        luck = int(input("Luck (1pt = +1 LUCK): "))

        playerstats = [health // 20, strength // 5, agility, shield, luck]
        if sum(playerstats) != 6:
            print("\nERROR: You must use exactly 6 points total!")
        else:
            playerCheating = False

    print(f"\nSTATS CONFIRMED:")
    print(f"HP: {health} | ATK: {strength} | DODGE: {agility}%")
    print(f"DEF: {shield} | LUCK: {luck}\n")

    # Story Intro
    print("\nThe year is 2245...")
    time.sleep(2)
    print("Humanity has colonized the solar system,")
    time.sleep(1.5)
    print("but something dark lurks in the void between worlds...")
    time.sleep(2)

    if difficulty == "easy":
        print("\nYou begin in a bustling city on Mars...")
        time.sleep(2)
        typing_animation("Traveling to lunar outpost...", delay=0.1)

        # Battle 1
        print("\nYou arrive at the moon. It looks eerie...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy")
        if new_weapon:
            current_weapon = new_weapon
        
        # Battle 2
        print("\nAfter the battle, you hear clicking noises...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy")
        if new_weapon:
            current_weapon = new_weapon
        
        # Battle 3
        print("\nYou press forward into the station...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy")
        if new_weapon:
            current_weapon = new_weapon

        # Final Battle
        print("\nAlarms blare as something approaches...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "medium")
        if new_weapon:
            current_weapon = new_weapon

    elif difficulty == "medium":
        print("\nYour ship receives a distress signal...")
        time.sleep(2)
        typing_animation("Approaching derelict station...", delay=0.1)

        # Battle sequence
        for i, desc in enumerate([
            "\nThe silent hangar feels wrong...",
            "\nFlickering lights reveal movement...",
            "\nYou find signs of violent struggle...",
            "\nEmergency systems suddenly activate..."
        ]):
            print(desc)
            time.sleep(2)
            health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "medium")
            if new_weapon:
                current_weapon = new_weapon
            if health <= 0:
                break

    elif difficulty == "hard":
        print("\nA ghost ship drifts in Saturn's rings...")
        time.sleep(2)
        typing_animation("Boarding the unknown vessel...", delay=0.1)

        # Battle sequence
        for i, desc in enumerate([
            "\nTotal darkness swallows you...",
            "\nOrganic growths pulse on the walls...",
            "\nThe temperature drops dangerously...",
            "\nEmergency lights reveal horrors..."
        ]):
            print(desc)
            time.sleep(2)
            health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "hard")
            if new_weapon:
                current_weapon = new_weapon
            if health <= 0:
                break

    # Game ending
    if health > 0:
        print("\nAgainst all odds, you survived this ordeal.")
        print("But the universe holds many more dangers...")
    else:
        print("\nYour journey ends here among the stars.")
    
    print("\nGame Over. Run the program to play again!")

if __name__ == "__main__":
    print("==== SPACE ODYSSEY RPG ====")
    print("Choose your game mode:")
    print("1. Easy Story Mode")
    print("2. Medium Story Mode")
    print("3. Hard Story Mode")
    print("4. Infinite Mode")
    
    while True:
        choice = input("Enter 1-4: ")
        if choice == "1":
            story_mode("easy")
            break
        elif choice == "2":
            story_mode("medium")
            break
        elif choice == "3":
            story_mode("hard")
            break
        elif choice == "4":
            infinite_mode()
            break
        else:
            print("Invalid choice! Please enter 1-4")