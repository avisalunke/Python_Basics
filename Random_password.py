import random

password=""
password_list=[]
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

numbers=['1','2','3','4','5','6','7','8','9','0']

symbols=['!','@','#','$','%','&','*']

nr_letters=int(input("how many letters you want in your passwords"))

nr_numbers=int(input("how many numbers you want in your password"))

nr_symbols=int(input("how many symbols you want in ypour password"))

for char in range(0,nr_letters):
    letter=random.choice(letters)
    password+=letter
    password_list.append(letter)

for num in range(0,nr_numbers):
    numb=random.choice(numbers)
    password+=numb
    password_list.append(numb)

for sys in range(0,nr_symbols):
    sys=random.choice(symbols)
    password+=sys
    password_list.append(sys)

random.shuffle(password_list)
# print(random.shuffle(password))

print(password)
password1=""
for char in password_list:
    password1+=char

print(password1)