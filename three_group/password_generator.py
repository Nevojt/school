import random
import string

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)



nr_letters = int(input(f"How many letters in your password?\n"))
nr_symbols = int(input(f"How many symbols in your password?\n"))
nr_numbers = int(input(f"How many numbers in your password?\n"))

random_letters = random.choices(letters, k=nr_letters)
random_symbols = random.choices(symbols, k=nr_symbols)
random_numbers = random.choices(numbers, k=nr_numbers)


list_password = random_letters + random_numbers + random_symbols
random.shuffle(list_password)

password = ''.join(list_password)
print(password)



