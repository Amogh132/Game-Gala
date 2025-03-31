import random

# Class to create armor with drop chance and stats
class Armor:
    def __init__(self, name, health, dropchance):
        self.name = name
        self.health = health
        self.dropchance = dropchance 

    def __repr__(self):
        return f"{self.name} (Health: {self.health}, Drop Chance: {self.dropchance})"

# List of armor types
armortypes = [
    Armor("Leather Armor", 20, 0.45),
    Armor("Steel Armor", 35, 0.15),
    Armor("Chain Mail Armor", 15, 0.65),
    Armor("Magic Armor", 80, 0.03)
]

# Function to drop an armor based on drop chance
def drop_armor():
    return random.choices(armortypes, weights=[armor.dropchance for armor in armortypes], k=1)[0]  # Pick 1 armor

# Simulate armor drops
armordrops = [drop_armor() for _ in range(4)]

print("Dropped Armor:", armordrops)
