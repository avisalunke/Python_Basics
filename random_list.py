import random

names_str=input("give me every bodys name whose card is in bowl..enter names by comma and space")

names=names_str.split(", ")

print(names)

length=len(names)
random_person_id=random.randint(0,length-1)

person_will_pay=names[random_person_id]


person_pay=random.choice(names)

print(f"this man  pay{person_pay}")
print(f"this man will pay{person_will_pay}")