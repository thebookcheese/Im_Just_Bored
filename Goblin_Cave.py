import random

def main(Player,Weapon):
    def Slash():
        Damage = random.randint(Weapon.attack - 1, Weapon.attack + 1)
        print("You dealt ",Damage," damage")
    def Chop():
        pass
    def Block():
        pass