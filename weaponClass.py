#make here a class that creates weapons their drop chance and the stats
class weapons:
    def __init__(self,name,damage,dropchance):
        self.name=name
        self.damage=damage
        self.damage=damage
        self.dropchance=dropchance

weapontypes = [
  weapons("beam saber",20,.45),
  weapons("plasma rifle",35,.15),
  weapons("energy shield",15,.65),
  weapons("light grenade",80,.03)  
]
