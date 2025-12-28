import random
import string

symbol_list = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '\\', '|', '`', '~'
]


while True:
    word1 = input("Enter a random word: ").strip()
    if any(char.isupper() for char in word1):
        break
    else:
        print("Please include at least one uppercase letter in your random word.")

word2 = input("Enter another word: ").strip()

while True:
    Numbers = input("Enter a series of numbers: ").strip()
    if Numbers.isdigit():
        break
    else:
     print("Please enter valid numbers.")


Symbol = random.choice(symbol_list)


password_parts = [word1, word2, Numbers, Symbol]
random.shuffle(password_parts)
password = ''.join(password_parts).replace('a', '@').replace('s', '$').replace('o', '0').replace('i', '1').replace('e','3')
print("Generated Password:", password)