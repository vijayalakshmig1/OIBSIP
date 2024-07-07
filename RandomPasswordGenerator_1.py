import random
import string
print("Welcome to Rrandom Password Generator!!!!")
length = int(input("Enter the length of the password: "))
letter = int(input("if you want letters then enter '1' or enter '0' : "))
digit = int(input("if you want digits then enter '1' or enter '0' : "))
punctuate = int(input("if you want punctuation then enter '1' or enter '0' : "))
characters=' '
if letter==1:
    characters += string.ascii_letters 
if digit==1:
    characters += string.digits 
if punctuate==1:
    characters += string.punctuation


def generate_password(length):
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage: Generate a password of length 14
generated_password = generate_password(length)
print("The Generated Password:", generated_password)