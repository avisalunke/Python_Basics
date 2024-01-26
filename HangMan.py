import random

word_list=["avinash","bapu","salunke"]


word=random.choice(word_list)

print(word)
blank = []
for i in range(0,len(word)):
    blank.append("_")

print(blank)
live=10
while "_" in blank and live != 0:
    letter=input("guess the letters")
    index=0
    for chare in word:
            if chare==letter:
                blank[index]=letter
                print(blank)
            else:
                 live-=1
                 print(live)
                 break
            index+=1
if "_" in blank and live==0:
    print("you loose")
else:
     print("you win")