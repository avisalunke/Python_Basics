import random

User_choice=int(input("please enter 0 for rock , 1 for scissor and 2 for paper"))

print("User Choice..")
print(User_choice)

computer_choice=random.randint(0,2)
0
print("Computer Choice")
print(computer_choice)

if User_choice < 0 or User_choice >2:
    print("invalid User Choice....")
else:
    # rock  >  scissor   0>1
    # paper >  rock    2>0
    # scissor > paper  1>2
    if User_choice==0 and computer_choice==1:
        print("User win")
    elif User_choice==1 and computer_choice==2:
        print("User Win")
    elif User_choice==2  and computer_choice==0:
        print("user win..")
    elif User_choice==computer_choice:
        print("match draw...")
    else:
        print("Computer win....")