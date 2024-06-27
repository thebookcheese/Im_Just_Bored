import Goblin_Cave

def main():
    class weapon():
        def __init__(self):
            self.Attack = 3
            self.WeaponType = "Sword"
            self.Reforge = ""
            self.ReforgeExtraAttack = 0
    class player():
        def ____init__(self):
            self.Phealth = 100
            self.Defense = 1
        
    Player = player()
    Weapon = weapon()

    def Shop():
        Buy = input("What do you want to buy? \n")
    def Blacksmith():
        BlacksmithDo = input("What do you want to do: \n Reforge (1) \n Melt (2) \n Upgrade (3)")
    def FinHouse():
        print("Imagine being lssssssssssssdddddsssddsdsdsds")
    def Travel():
        Go = input("Where do you wnat to go: \n FinHouse (1) \n Goblin Cave (2) \n Haunted house (3)")
        if Go == "1":
            FinHouse()
        elif Go == "2":
            Goblin_Cave.main(Player,Weapon)
        elif Go == "3":
            pass