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
    "Giant": PlayerClass("Giant", 150, 25, 10, 15, "Crush"),
    "Tank": PlayerClass("Tank", 200, 15, 5, 25, "Barrier"),
    "Speedster": PlayerClass("Speedster", 100, 20, 30, 10, "Dash"),
    "Warrior": PlayerClass("Warrior", 120, 30, 15, 15, "Berserk"),
    "Gambler": PlayerClass("Gambler", 110, 15, 15, 15, "Jackpot")
}

def get_class_stats(class_name):
    return classes.get(class_name, classes["Warrior"])  # Default to Warrior if invalid