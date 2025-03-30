import random

class Mob:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

enemy_template = [
    Mob("Mad Scientist", 10, 15),
    Mob("Drone", 6, 15),
    Mob("Cyborg", 12, 12),
    Mob("Mecha", 4, 70),
    Mob("Alien", 15, 30),
    Mob("Space Pirate", 12, 22),
    Mob("Parasite", 4, 8),
    Mob("Raider", 8, 30),
    Mob("UFO", 12, 35),
    Mob("Tentacle", 20, 17),
    Mob("Alien Beast", 30, 50),
    Mob("Guard", 10, 28),
    Mob("Mutant", 15, 20),
    Mob("Bounty Hunter", 25, 20),
    Mob("Turret", 27, 14),
]

def spawn_enemy():
    """Selects and returns a random enemy"""
    return random.choice(enemy_template)

def display_enemy(enemy):
    """Outputs the enemy stats"""
    print(f"Name: {enemy.name}")
    print(f"Health: {enemy.health}")
    print(f"Attack: {enemy.attack}")

def enemy_encounter():
    """Handles enemy encounter logic"""
    while True:
        choice = input("Are you ready for the enemy? (y/n): ").strip().lower()
        
        if choice == "y":
            print("\nAn enemy is approaching...\n")
            enemy = spawn_enemy()
            display_enemy(enemy)
            print("\nGood luck!\n")
            break
        elif choice == "n":
            print("\nCome back when you're ready!\n")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
