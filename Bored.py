import random
import RPGmain

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
    Card3 = 0
    Card4 = 0
    Count = 0
    StoodCount = 0
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
    print("You got ",Card1," and ",Card2)
    while (Card1 + Card2 + Card3 + Card4) != 21 or (Card1 + Card2 + Card3 + Card4) < 21 or (AiCard1 + AiCard2 + AiCard3 + AiCard4) != 21 or (AiCard1 + AiCard2 + AiCard3 + AiCard4) < 21:
        if (Card1 + Card2 + Card3) > 21:
            print("Bust, you lose.")
            exit()
        elif (Card1 + Card2 + Card3) < 21:
            Pick = int(input("Do you want to twist (1) or stick (2)"))
            OriginalPick = Pick
            if Pick == 1:
                if Count == 0:
                    Card3 = random.randint(1,10)
                    Count = Count + 1
                    if (Card1 + Card2 + Card3 + Card4) > 21:
                        print("Bust, you lose")
                        exit()
                    elif (Card1 + Card2 + Card3 + Card4) == 21:
                        print("You win")
                        exit()
                    else:
                        print("You got ",Card3)
                        Pick = 2
                elif Count == 1:
                    Card4 = random.randint(1,10)
                    Count = Count + 1
                    if (Card1 + Card2 + Card3 + Card4) > 21:
                        print("Bust, you lose")
                        exit()
                    elif (Card1 + Card2 + Card3 + Card4) == 21:
                        print("You win")
                        exit()
                    else:
                        print("You got ",Card4)
                        Pick = 2
            elif Pick == 2:
                if OriginalPick == 2:
                    StoodCount = StoodCount + 1
                else:
                    pass
                AiCard1 = random.randint(1,11)
                AiCard2 = random.randint(1,11)
                AiCard3 = 0
                AiCard4 = 0
                AiStoodCount = 0
                if AiCard1 == 11:
                    if (AiCard2 + 1) == 21:
                        AiCard1 = 1
                    elif (AiCard2 + 10) == 21:
                        AiCard1 = 10
                    else:
                        AiCard1 = 10
                else:
                    pass
                if AiCard2 == 11:
                    if (AiCard1 + 1) == 21:
                        AiCard2 = 1
                    elif (AiCard1 + 10) == 21:
                        AiCard2 = 10
                    else:
                        AiCard2 = 10
                else:
                    pass
                if (AiCard1 + AiCard2 + AiCard3) > 21:
                    print("You win!")
                    exit()
                elif (AiCard1 + AiCard2 + AiCard3) == 21:
                    print("Ai Won, you lost")
                else:
                    pass
                if (21 - (AiCard1 + AiCard2 + AiCard3)) > 10 and (21 - (AiCard1 + AiCard2 + AiCard3)) < 15:
                    AiCard3 = random.randint(1,10)
                    if (AiCard1 + AiCard2 + AiCard3) == 21:
                        print("Ai wins, you lose")
                        exit()
                    elif (AiCard1 + AiCard2 + AiCard3) > 21:
                        print("Ai bust, you win!")
                    else:
                        pass
                else:
                    print("Ai stood")
                    AiStoodCount = AiStoodCount + 1
                    if AiStoodCount == 1 and StoodCount == 1:
                        if (Card1 + Card2 + Card3 + Card4) > 21:
                            print("You lose")
                            exit()
                        elif (21 -(Card1 + Card2 + Card3 + Card4)) > (21 - (AiCard1 + AiCard2 + AiCard3 + AiCard4)):
                            print("You lose")
                            exit()
                        elif (21 - (Card1 + Card2 + Card3 + Card4)) < (21 - (AiCard1 + AiCard2 + AiCard3 + AiCard4)):
                            print("You win")
                            exit()
                        elif (Card1 + Card2 + Card3 + Card4) == 21 and (AiCard1 + AiCard2 + AiCard3 + AiCard4) == 21:
                            print("Draw")
                            exit()
                        elif (Card1 + Card2 + Card3 + Card4) == 21:
                            print("You win")
                            exit()
                        elif (AiCard1 + AiCard2 + AiCard3 + AiCard4) == 21:
                            print("You lose")
                            exit()
                    else:
                        StoodCount = 0
                        AiStoodCount = 0



def RPG_but_bad():
    RPGmain.main()
    
Run = int(input("Software run? \n Dice Thing (1) \n Blackjack (2) \n"))
if Run == 1:
    Dice()
elif Run == 2:
    Blackjack()
else:
    print("Go away then")
    exit()