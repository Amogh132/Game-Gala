import random

class Mob:
    def __init__(self, name, attack, health, difficulty):
        self.name = name
        self.attack = attack
        self.health = health
        self.difficulty = difficulty  # 'easy', 'medium', or 'hard'

# Base enemy templates (medium difficulty)
enemy_templates = [
    Mob("Mad Scientist", 10, 15, "medium"),
    Mob("Drone", 6, 15, "medium"),
    Mob("Cyborg", 12, 12, "medium"),
    Mob("Mecha", 4, 70, "medium"),
    Mob("Alien", 15, 30, "medium"),
    Mob("Space Pirate", 12, 22, "medium"),
    Mob("Parasite", 4, 8, "easy"),
    Mob("Raider", 8, 30, "medium"),
    Mob("UFO", 12, 35, "medium"),
    Mob("Tentacle", 20, 17, "hard"),
    Mob("Alien Beast", 30, 50, "hard"),
    Mob("Guard", 10, 28, "medium"),
    Mob("Mutant", 15, 20, "medium"),
    Mob("Bounty Hunter", 25, 20, "hard"),
    Mob("Turret", 27, 14, "hard")
]

def enemy_encounter(difficulty="medium"):
    # Filter enemies by difficulty
    filtered_enemies = [e for e in enemy_templates if e.difficulty == difficulty]
    
    # If no enemies for this difficulty, scale medium enemies
    if not filtered_enemies:
        filtered_enemies = [e for e in enemy_templates if e.difficulty == "medium"]
    
    base_enemy = random.choice(filtered_enemies)
    
    # Scale stats based on difficulty
    if difficulty == "easy":
        return Mob(
            f"Weak {base_enemy.name}",
            max(1, int(base_enemy.attack * 0.7)),
            max(5, int(base_enemy.health * 0.8)),
            difficulty
        )
    elif difficulty == "hard":
        return Mob(
            f"Elite {base_enemy.name}",
            int(base_enemy.attack * 1.5),
            int(base_enemy.health * 1.4),
            difficulty
        )
    else:
        return Mob(
            base_enemy.name,
            base_enemy.attack,
            base_enemy.health,
            difficulty
        )

class Weapon:
    def __init__(self, name, damage, drop_chance):
        self.name = name
        self.damage = damage
        self.drop_chance = drop_chance

    def __repr__(self):
        return f"{self.name} (Damage: +{self.damage})"

weapon_types = [
    Weapon("Beam Saber", 5, 0.45),
    Weapon("Plasma Rifle", 10, 0.15),
    Weapon("Energy Shield", 3, 0.65),
    Weapon("Light Grenade", 15, 0.03)
]

def get_random_weapon():
    return random.choices(
        weapon_types,
        weights=[w.drop_chance for w in weapon_types],
        k=1
    )[0]

def get_infinite_enemy(level):
    base_enemies = [
        Mob("Hive Drone", 15, 50),
        Mob("War Cyborg", 25, 80),
        Mob("Alpha Alien", 35, 120),
        Mob("Doom Mech", 50, 200)
    ]
    enemy = random.choice(base_enemies)
    scaled_attack = enemy.attack * (1 + (level // 7))
    scaled_health = enemy.health * (1 + (level // 5))
    return Mob(
        f"Lv{level} {enemy.name}",
        int(scaled_attack),
        int(scaled_health),
        "infinite"
    )

def get_boss(level):
    return Mob(
        f"★★★ Boss {level} ★★★",
        50 + (level * 10),
        300 + (level * 50),
        "boss"
    )

# Update weapon generation for infinite mode
def get_random_weapon(level=1):
    weapons = [
        Weapon("Beam Saber", 5 + level, 0.45),
        Weapon("Plasma Rifle", 10 + level*2, 0.15),
        Weapon("Energy Shield", 3 + level, 0.65),
        Weapon("Light Grenade", 15 + level*3, 0.03)
    ]
    return random.choices(weapons, weights=[w.drop_chance for w in weapons])[0]



def apply_class_bonuses(player_stats, player_class):
    """Apply class bonuses to player stats"""
    player_stats['health'] += player_class.base_health
    player_stats['strength'] += player_class.base_attack
    player_stats['agility'] += player_class.base_agility
    player_stats['shield'] += player_class.base_shield
    return player_stats