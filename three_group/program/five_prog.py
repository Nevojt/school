"""1. Програма з функціями: Гра "Вгадай число"
Ця гра демонструє, як можна використовувати функції для розділення логіки програми на кілька частин"""


import random

def get_user_guess():
    return int(input("Вгадай число від 1 до 10: "))

def check_guess(guess, answer):
    if guess == answer:
        print("Вітаю, ти вгадав!")
        return True
    elif guess < answer:
        print("Замало, спробуй ще раз.")
    else:
        print("Забагато, спробуй ще раз.")
    return False

def guess_number_game():
    answer = random.randint(1, 10)
    attempts = 0
    while attempts < 3:
        guess = get_user_guess()
        if check_guess(guess, answer):
            break
        attempts += 1
    else:
        print(f"На жаль, ти не вгадав. Правильна відповідь була {answer}.")

guess_number_game()


"""2. Програма зі списками: Підрахунок символів
Ця програма показує, як можна використовувати списки для зберігання даних і простий перебір для аналізу тексту."""

# def count_characters(text):
#     count = []
#     for char in set(text):
#         count.append((char, text.count(char)))
#     return count

# text = input("Введіть текст: ")
# char_counts = count_characters(text)
# print("Кількість кожного символу в тексті:")
# for char, count in char_counts:
#     print(f"'{char}': {count}")

"""3. Програма зі списковими включеннями: Знаходження парних чисел
Ця програма використовує спискові включення для фільтрації даних у списку."""

# def find_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = find_even_numbers(numbers)
# print("Парні числа:", even_numbers)


"""4. Програма зі списковими включеннями: Знаходження непарних чисел
Ця програма використовує спискові включення для фільтрації даних у списку."""

# def add_book(library, title, author):
#     library[title] = author

# def print_library(library):
#     for title, author in library.items():
#         print(f"Книга '{title}' написана {author}.")

# library = {}
# add_book(library, "Гаррі Поттер", "Дж. К. Роулінг")
# add_book(library, "Володар Перснів", "Дж. Р. Р. Толкієн")
# print_library(library)


"""5. Програма для вивчення таблиці множення
Ця програма використовує функції та списки для створення інтерактивної таблиці множення."""

# def print_multiplication_table(size):
#     for i in range(1, size+1):
#         row = [i * j for j in range(1, size+1)]
#         print(" ".join(str(x) for x in row))

# table_size = int(input("Введіть розмір таблиці множення: "))
# print_multiplication_table(table_size)
