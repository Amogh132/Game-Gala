#Making Player Classes

class Player:
  def __init__(self , className, uniqueSkills1, uniqueSkills2, uniqueSkills3, uniqueSkills4):
    self.className = className
    self.uniqueSkills1 = uniqueSkills1
    self.uniqueSkills2 = uniqueSkills2
    self.uniqueSkills3 = uniqueSkills3
    self.uniqueSkills4 = uniqueSkills4

giant = Player("Giant", 5, 4, 5, "Heal") # when making player classes follow this template
tank = Player("Tank", 3, 6, 5, "Barrier")
speedster = Player("Speedster", 4, 3, 7, "Sprint") # Idk if we want that to be a dash instead
warrior = Player("Warrior", 6, 4, 4, "Beserk")
gambler = Player("Gambler", 4, 4, 4, "Spin") # We could change that to another word for the skill, like gamble or smt

