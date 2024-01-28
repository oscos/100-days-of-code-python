#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!

password = ""

for n in range(0,nr_letters):
    random_number = random.randint(0,25)
    selected_char = letters[random_number]
    password += selected_char
# print(selected_letters)

for n in range(0,nr_symbols):
    random_number = random.randint(0,8)
    selected_char = symbols[random_number]
    password += selected_char
# print(selected_symbols)

for n in range(0,nr_numbers):
    random_number = random.randint(0,9)
    selected_char = numbers[random_number]
    password += selected_char
# print(selected_numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in password:
  password_list.append(char)
# print(password_list)

random.shuffle(password_list) # mutates original list
# print(password_list)

password_shuffled = ""
for char in password_list:
  password_shuffled += char
print(password_shuffled)


