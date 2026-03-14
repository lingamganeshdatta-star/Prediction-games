import random
import string
import sys

def generate_password(length=1):
    characters=string.ascii_letters+string.digits+string.punctuation
    sample=''.join(random.choice(characters) for _ in range(length))
    return sample
while True:
    length=int(input("enter the length of the pasword"))
    password=generate_password(length)
    print(password)
    choice=input("Do you wnat this password?(yes/no)").lower()
    if choice=="yes":
        print("password accepted")
        break
    else:
        print("Generating password......")
    
