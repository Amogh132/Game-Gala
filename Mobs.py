import random

class Mobs:
  def __init__(self,name,attack,health):
    self.name = name
    self.attack = attack
    self.health = health


class boss:
  def __init__(self,name,health,attack,move1,move2,move3):
    self.name = name
    self.health = health
    self.attack = attack
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3


enemy_template = [
  Mobs("Mad scientist",10,15),
  Mobs("Drone",6,15),
  Mobs("Cyborg",12,12),
  Mobs("Mecha",4,70),
  Mobs("Alien",15,30),
  Mobs("Space Pirate",12,22),
  Mobs("Parasite",4,8),
  Mobs("Raider",8,30),
  Mobs("UFO",12,35),
  Mobs("Tentacle",20,17),
  Mobs("Alien Beast",30,50),
  Mobs("Guard",10,28),
  Mobs("Mutant",15,20),
  Mobs("Bounty hunter",25,20),
  Mobs("Turret",27,14),
  
]

boss_template = [
  boss("boss1",100,50, 20,10,40)
  ]


def spawn_enemy():
  '''
  selects enemy type
  '''
  enemy = random.choice(enemy_template)
  return enemy


def display_enemy(enemy):
  '''
  Outputs the enemy stats
  '''
  print(f"Name: {enemy.name}")
  print(f"Health: {enemy.health}")
  print(f"Attack: {enemy.attack}")


choice = input("Are you ready for the enemy? y or n: ")
if choice == "y":
  print("ok,enemy is approaching")
  enemy = spawn_enemy()
  display_enemy(enemy)
  print("Good Luck Bud")
else:
  print("Invalid Choice.")
  choice = input("Are you ready for the enemy? y or n: ")







