import random

def Dice():
    Roll1 = random.randint(1,6)
    Roll2 = random.randint(1,6)
    if Roll1 == Roll2:
        print("Duos!")
    elif Roll1 == 7 and Roll1 == Roll2:
        print("Sevens!")
    else:
        print("You got nothing")

def Blackjack():
    Card1 = random.randint(1,11)
    Card2 = random.randint(1,11)
    if Card1 == 11:
        Ace = input("Should it be a 1 or 10 \n Type 1 if 1 \n Type 2 if 10")        
        if Ace == 1:
            Card1 = 1
        elif Ace == 2:
            Card1 = 10
        else:
            exit()
    elif Card2 == 11:
        Ace = input("Should it be a 1 or 10 \n Type 1 if 1 \n Type 2 if 10")        
        if Ace == 1:
            Card1 = 1
        elif Ace == 2:
            Card1 = 10
        else:
            exit()
    else:
        pass
    while (Card1 + Card2) is not 21 or (Card1 + Card2) < 21:
        if (Card1 + Card2) > 21:
            print("Bust, you lose.")
            exit()
        elif (Card1 + Card2) < 21:
            Pick = input("Do you want to twist (1) or stick (2)")
            if Pick == 1:
                Card3 = random.randint(1,10)
            elif Pick == 2:
                AiCard1 = random.randint(1,11)
                AiCard2 = random.randint(1,11)
                if (AiCard1 + AiCard2) > 21:
                    print("You win!")
                    exit()
                elif (AiCard1 + AiCard2) == 21:
                    print("Ai Won, you lost")
                else:
                    pass



Run = input("Software run? \n Dice Thing (1) \n")
if Run == 1:
    Dice()
else:
    pass