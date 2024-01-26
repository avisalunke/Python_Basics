def add(n1,n2):
    return n1+n2


def substract(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2


operarions = {
    "+":add,
    "-":substract,
    "*":multiplication,
    "/":devide
}
    

n1=int(input("whats the first number ? "))
n2=int(input("whats the second number ? "))

for symbol in operarions:
    print(symbol)

should_continu=True

while should_continu:
    your_symbol=input("pick an operation from above")
    operarions_function=operarions[your_symbol]
    answer=operarions_function(n1,n2)
    print(f"{n1} {your_symbol} {n2} = {answer}")
    conti= input(f"if you want to continu with {answer} then type 'y' if you want exit then type 'n'").lower()
    if conti=="y":
        n1=answer
    else:
        should_continu=False