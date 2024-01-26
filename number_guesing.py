import random
import art

print(art.logo)

print("wlcome to the number guessing game!!!...")
print("I am thinking of a number between 1 to 100....")

difficulty=input("choose a difficulty type 'easy' or 'hard' :").lower()
if difficulty=="easy":
    lives=10
if difficulty =="hard":
    lives=5
number=random.randint(1,100)
while lives > 0:
    print(f"you have {lives} attempt remaining to guess the number..")
    your_number=int(input("make a guess :"))
    if your_number>number:
        print("too high")
        lives-=1
    if your_number<number:
        print("too low")
        lives-=1
    if your_number==number:
        print(f"you got it ! the answer was {number}")
        break
     