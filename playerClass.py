#Making Player Classes

class Player:
  def __init__(self , className, uniqueSkills1, uniqueSkills2, uniqueSkills3, uniqueSkills4):
    self.className = className
    self.uniqueSkills1 = uniqueSkills1
    self.uniqueSkills2 = uniqueSkills2
    self.uniqueSkills3 = uniqueSkills3
    self.uniqueSkills4 = uniqueSkills4

giant = Player("Giant", 5, 4, 5, "Heal") # when making player classes follow this template
#tank = Player()
#speedster = Player()
#warrior = Player()
#gambler = Player()

