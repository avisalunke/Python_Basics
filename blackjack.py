import random

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

user_cards=[]
computer_cards=[]

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

def calculate_score(cards1):
    print(computer_cards)
    if sum(cards1)==21 and len(cards1)==2 :
      return 0 
    if 11 in cards1 and sum(cards1)>21:
        cards1.remove(11)
        cards1.append(1)
    return sum(cards1)


def compare(user_score,computer_score):
    if user_score == computer_score:
        return "DRAW.."
    elif computer_score==0:
        return "you lose..Oppenent has Black jack.."
    elif user_score ==0:
        return "you win..you have black jack.."
    elif user_score>21:
        return "you loose , you went over 21"
    elif computer_score>21:
        return " you win , oppenent went over"
    elif user_score>computer_score:
        return "you win .."
    else:
        return "you loose.."

is_game_over=False

while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f" user cards : {user_cards} , user score :{user_score}")
    print(f" computer first card : {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("type 'y' to get another card type 'n' to pass").lower()
        if user_should_deal=='y':
            user_cards.append(deal_cards())
            print(user_cards)
        else:
            is_game_over=True
    
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_cards)
        computer_score=calculate_score(computer_cards)

print(f" user final cards : {user_cards} , user score :{user_score}")
print(f" computer final cards : {computer_cards} , computer score :{computer_score}")
print(compare(user_score,computer_score))