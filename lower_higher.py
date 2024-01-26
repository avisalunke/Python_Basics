import art
from data import Idata 
import random

print(art.logo)

game_over=False
Score=0
while not game_over:
    celebA=Idata[random.randint(0,len(Idata)-1)]
    celebB=Idata[random.randint(0,len(Idata)-1)]
    while celebA == celebB:
        celebB=Idata[random.randint(0,len(Idata)-1)]
    print(f"Compare A: {celebA['name']}")
    print(art.vs)
    print(f"Against B: {celebB['name']}")
    answer=input("who has more followers? type 'A' or 'B' :  ")
    if answer=="A" and celebA["followers"]>celebB["followers"]:
        Score+=1
        print(f"you are right!!..current score is: {Score}")
    elif answer=="B" and celebA["followers"]<celebB["followers"]:
        Score+=1
        print(f"Sorry ..your current score is {Score}")
    else:
        print(f"Sorry ..your Final score is {Score}")
        game_over=True



