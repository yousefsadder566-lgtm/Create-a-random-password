import random
import string
print("Welcome to the password Generator! ")
characters=int(input("Enter the total number of characters in the password: "))
letters=int(input("Enter the number of letters in the password: "))
numbers=int(input("Enter the numbers in the password: "))
symbols=int(input("Enter the number of symbols in the password: "))
if letters+numbers+symbols!=characters:
    print("Invalid input. The sum of letters, numbers, and symbols doesnt match the password")
    exit()
a=random.choices(string.ascii_letters,k=letters)
b=random.choices(string.digits,k=numbers)
c=random.choices(string.punctuation,k=symbols)
listt=[]
listt.extend(a)
listt.extend(b)
listt.extend(c)
done1=random.choices(listt,k=len(listt))
done="".join(done1)
print("Generated Password:",done)
