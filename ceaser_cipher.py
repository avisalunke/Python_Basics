letters=[ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


your_choice=input("please enter encode or decode").lower()
your_text=input("please enter text...")
print(your_choice,your_text)
your_shift=int(input("enter your shift number.."))


def encryption():
    print("encryption..")
    encrypted=""
    for char in your_text:
        number=letters.index(char)+your_shift
        if number>26:
            number-=25
        encrypted+=letters[number]
    print(encrypted)  


def decryption():
    print("decryption...")
    decrypted=""
    for char in your_text:
        number=letters.index(char)-your_shift
        if number<0:
            number+=25
        decrypted+=letters[number]
    print(decrypted) 
  
if your_choice=="encode":
    encryption()
if your_choice=="decode":
    decryption()