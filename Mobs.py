import random

class Mobs:
  def __init__(self,name,health,attack):
    self.name = name
    self.health = health
    self.attack = attack


enemy_template = [
  Mobs("bandit",6,4),
  Mobs("Raider",7,5),
  Mobs("Tank",23,3),
  Mobs("Necromancer",6,7),
]

def spawn_enemy():
  enemy = random.choice(enemy_template)
  return enemy

def display_enemy(self):
  print(f"Name: {self.name}")
  print(f"Health: {self.health}")
  print(f"Attack: {self.attack}")





