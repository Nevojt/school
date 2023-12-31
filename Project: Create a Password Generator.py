#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


#Easy Level - Order not randomized:

letters_list = []
numbers_list = []
symbols_list = []

for i in range(nr_letters):
  run = random.choice(letters)
  letters_list += run
  random_letters = ''.join(letters_list)

for i in range(nr_numbers):
  runs = random.choice(numbers)
  numbers_list += runs
  random_numbers = ''.join(numbers_list)  

for i in range(nr_symbols):
  runs = random.choice(symbols)
  symbols_list += runs
  random_symbols = ''.join(symbols_list)  

list_light = random_letters + random_numbers + random_symbols
print(list_light)


#Hard Level - Order of characters randomized:

list_hard = ''.join(random.sample(list_light, len(list_light)))
print(list_hard)


# password = int(input("Password: "))

# hack = 0
# for i in range(0, 100000000):
#     hack += 1
#     if password == hack:
#         print(f"Your password {password}")
        
        
# import itertools
# import string

# # Пароль, який потрібно знайти
# password = "Hello"

# # Генеруємо можливі комбінації з англійських літер
# for attempt in itertools.product(string.ascii_letters, repeat=5):
#     try_pass = ''.join(attempt)
#     if try_pass == password:
#         print("Пароль знайдено:", try_pass)
#         break
        
import string
import random

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)


nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = random.choices(letters, k=nr_letters)
random_symbols = random.choices(symbols, k=nr_symbols)
random_numbers = random.choices(numbers, k=nr_numbers)

list_password = random_letters + random_symbols + random_numbers
random.shuffle(list_password)
password = ''.join(list_password)
print(password)
