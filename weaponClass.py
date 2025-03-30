#make here a class that creates weapons their drop chance and the stats
import random

# Class to create weapons with drop chance and stats
class Weapon:
    def __init__(self, name, damage, dropchance):
        self.name = name
        self.damage = damage
        self.dropchance = dropchance 

    def __repr__(self):
        return f"{self.name} (Damage: {self.damage}, Drop Chance: {self.dropchance})"

# List of weapon types
weapontypes = [
    Weapon("Beam Saber", 20, 0.45),
    Weapon("Plasma Rifle", 35, 0.15),
    Weapon("Energy Shield", 15, 0.65),
    Weapon("Light Grenade", 80, 0.03)
]

# Function to drop a weapon based on drop chance
def drop_weapon():
    weapon_names = [weapon.name for weapon in weapontypes]
    drop_chances = [weapon.dropchance for weapon in weapontypes]
    return random.choices(weapon_names, weights=drop_chances, k=1)[0]  # Pick 1 weapon


weapondrops = [drop_weapon() for _ in range(4)]

print("Dropped Weapons:", weapondrops)
