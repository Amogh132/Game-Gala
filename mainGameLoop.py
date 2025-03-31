import time
import random
import sys
import Mobs

class PlayerClass:
    def __init__(self, name, base_health, base_attack, base_agility, base_shield, special_ability):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_agility = base_agility
        self.base_shield = base_shield
        self.special_ability = special_ability

# Define classes
classes = {
    "Giant": PlayerClass("Giant", 50, 10, 5, 5, "Crush"),
    "Tank": PlayerClass("Tank", 80, 5, 3, 15, "Barrier"),
    "Speedster": PlayerClass("Speedster", 40, 8, 15, 3, "Dash"),
    "Warrior": PlayerClass("Warrior", 60, 15, 8, 8, "Berserk"),
    "Gambler": PlayerClass("Gambler", 50, 7, 7, 7, "Jackpot")
}

def select_class():
    print("\n=== CHOOSE YOUR CLASS ===")
    print("1. Giant - High power, low speed (+50 HP, +10 ATK)")
    print("2. Tank - Extreme defense (+80 HP, +15 DEF)")
    print("3. Speedster - Lightning fast (+15 AGI)")
    print("4. Warrior - Balanced fighter (+15 ATK, +8 AGI/DEF)")
    print("5. Gambler - High risk/reward (Random effects)")
    
    while True:
        choice = input("Select class (1-5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            return list(classes.values())[int(choice)-1]
        print("Invalid choice!")

def battle_loop(player_health, player_strength, player_agility, player_shield, enemy, current_weapon, player_class):
    print(f"\nA {enemy.name} has appeared!\n")
    
    # Class ability variables
    berserk_turns = 0
    barrier_active = False
    crush_cooldown = 0
    dash_available = True
    
    if current_weapon:
        print(f"Equipped Weapon: {current_weapon.name} (+{current_weapon.damage} damage)")
    
    blocked_damage = 0
    
    while player_health > 0 and enemy.health > 0:
        print(f"\nYour Health: {player_health}")
        print(f"{enemy.name} Health: {enemy.health}")
        
        # Display available actions
        actions = "[A]ttack [D]efend [O]dodge"
        if player_class.special_ability == "Crush" and crush_cooldown == 0:
            actions += " [C]rush"
        elif player_class.special_ability == "Barrier" and not barrier_active:
            actions += " [B]arrier"
        elif player_class.special_ability == "Dash" and dash_available:
            actions += " [D]ash"
        elif player_class.special_ability == "Berserk" and berserk_turns == 0:
            actions += " [B]erserk"
        elif player_class.special_ability == "Jackpot":
            actions += " [J]ackpot"
            
        action = input(f"{actions}: ").strip().lower()
        
        # Handle special abilities
        if action in ["c", "b", "j"] and player_class.special_ability.lower().startswith(action):
            if action == "c" and crush_cooldown == 0:  # Giant's Crush
                damage = int((player_strength + (current_weapon.damage if current_weapon else 0)) * 1.5)
                enemy.health -= damage
                crush_cooldown = 3
                print(f"\n💥 CRUSH! You smash for {damage} damage!")
            elif action == "b":  # Tank's Barrier
                if not barrier_active:
                    player_shield += 10
                    barrier_active = True
                    print("\n🛡️ BARRIER! +10 defense!")
                else:
                    print("\nBarrier already active!")
            elif action == "d" and dash_available:  # Speedster's Dash
                dash_available = False
                print("\n💨 DASH! You'll dodge next attack!")
            elif action == "b" and berserk_turns == 0:  # Warrior's Berserk
                berserk_turns = 3
                print("\n⚡ BERSERK! Double damage for 3 turns!")
            elif action == "j":  # Gambler's Jackpot
                result = random.choice(["heal", "double", "instakill"])
                if result == "heal":
                    player_health += 30
                    print("\n🎰 Jackpot! Healed 30 HP!")
                elif result == "double":
                    damage = (player_strength + (current_weapon.damage if current_weapon else 0)) * 2
                    enemy.health -= damage
                    print(f"\n🎰 Jackpot! Double damage: {damage}!")
                else:
                    if random.random() < 0.3:
                        enemy.health = 0
                        print("\n🎰 JACKPOT! Instant KO!")
                    else:
                        print("\n🎰 Jackpot failed!")
            continue
        
        # Normal combat actions
        if action == "a":
            damage = player_strength + random.randint(0, 5)
            if current_weapon:
                damage += current_weapon.damage
            if berserk_turns > 0:
                damage *= 2
            enemy.health -= damage
            print(f"\nYou attack the {enemy.name} for {damage} damage!")

        elif action == "d":
            blocked_damage = player_shield + random.randint(1, 3)
            if barrier_active:
                blocked_damage += 10
            if current_weapon and current_weapon.name == "Energy Shield":
                blocked_damage += 2
            print(f"\nYou brace yourself, preparing to absorb {blocked_damage} damage.")

        elif action == "o":
            dodge_chance = min(90, player_agility * 10)
            if action == "d" and not dash_available:  # Dash dodge
                print("\n💨 Dash dodges automatically!")
                dash_available = True
                continue
            elif random.randint(1, 100) <= dodge_chance:
                print(f"\nYou swiftly dodge the {enemy.name}'s attack!")
                continue
            else:
                print("\nYou failed to dodge!")

        # Enemy attack
        if enemy.health > 0:
            enemy_damage = enemy.attack - (blocked_damage if action == "d" else 0)
            enemy_damage = max(0, enemy_damage)
            player_health -= enemy_damage
            print(f"The {enemy.name} strikes back, dealing {enemy_damage} damage!")

        # Update cooldowns
        if berserk_turns > 0:
            berserk_turns -= 1
            if berserk_turns == 0:
                print("\nBerserk effect wore off")
        if crush_cooldown > 0:
            crush_cooldown -= 1

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

def spawn_enemy(player_health, player_strength, player_agility, player_shield, current_weapon, difficulty, player_class):
    if difficulty == "infinite":
        enemy = Mobs.get_infinite_enemy(player_strength)
    else:
        enemy = Mobs.enemy_encounter(difficulty)
    result = battle_loop(player_health, player_strength, player_agility, player_shield, enemy, current_weapon, player_class)
    return result["player_health"], result["weapon_dropped"]

def infinite_mode(player_class):
    current_weapon = None
    health = 100 + player_class.base_health
    strength = 15 + player_class.base_attack
    agility = 5 + player_class.base_agility
    shield = 5 + player_class.base_shield
    level = 1
    boss_counter = 0

    print(f"\n=== INFINITE MODE - {player_class.name} ===")
    print(f"Special Ability: {player_class.special_ability}")
    print("Survive as long as you can!")
    print("Every 5 levels you'll face a powerful boss!\n")
    time.sleep(2)

    while True:
        print(f"\n=== LEVEL {level} ===")
        
        if level % 5 == 0:
            enemy = Mobs.get_boss(level)
            boss_counter += 1
        else:
            enemy = Mobs.get_infinite_enemy(level)
        
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "infinite", player_class)
        
        if health <= 0:
            print(f"\nYou survived {level} levels!")
            print(f"Defeated {boss_counter} bosses!")
            break
        
        if new_weapon:
            current_weapon = new_weapon
        
        # Progressive difficulty
        level += 1
        strength += 2
        health += 25 + (level % 5)
        agility += 1
        shield += 1

        if level % 5 == 0:
            print("\n⭐ Level Bonus! +50 HP and +5 ATK!")
            health += 50
            strength += 5

def story_mode(difficulty, player_class):
    username = ""
    health = 0 + player_class.base_health
    strength = 0 + player_class.base_attack
    agility = 0 + player_class.base_agility
    shield = 0 + player_class.base_shield
    luck = 0
    current_weapon = None

    print(f"Welcome to SPACE ODYSSEY RPG - {player_class.name}!")
    time.sleep(0.5)
    username = input("Enter your name: ")
    time.sleep(0.5)
    print(f"\nWelcome {username}! (Class: {player_class.name})")
    print(f"Special Ability: {player_class.special_ability}")
    print("Distribute 6 points between your stats.")
    time.sleep(0.5)

    playerCheating = True
    while playerCheating:
        print("\n--- STAT DISTRIBUTION ---")
        health += int(input("Health (1pt = +20 HP): ")) * 20
        strength += int(input("Strength (1pt = +5 ATK): ")) * 5
        agility += int(input("Agility (1pt = +1 DODGE): "))
        shield += int(input("Shield (1pt = +1 DEF): "))
        luck = int(input("Luck (1pt = +1 LUCK): "))

        playerstats = [(health-player_class.base_health)//20, 
                      (strength-player_class.base_attack)//5, 
                      agility-player_class.base_agility, 
                      shield-player_class.base_shield, 
                      luck]
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
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy", player_class)
        if new_weapon:
            current_weapon = new_weapon
        
        # Battle 2
        print("\nAfter the battle, you hear clicking noises...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy", player_class)
        if new_weapon:
            current_weapon = new_weapon
        
        # Battle 3
        print("\nYou press forward into the station...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "easy", player_class)
        if new_weapon:
            current_weapon = new_weapon

        # Final Battle
        print("\nAlarms blare as something approaches...")
        time.sleep(2)
        health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "medium", player_class)
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
            health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "medium", player_class)
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
            health, new_weapon = spawn_enemy(health, strength, agility, shield, current_weapon, "hard", player_class)
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
    
    player_class = select_class()
    
    while True:
        choice = input("Enter 1-4: ")
        if choice == "1":
            story_mode("easy", player_class)
            break
        elif choice == "2":
            story_mode("medium", player_class)
            break
        elif choice == "3":
            story_mode("hard", player_class)
            break
        elif choice == "4":
            infinite_mode(player_class)
            break
        else:
            print("Invalid choice! Please enter 1-4")