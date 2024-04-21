# TODO:
#  1. Work home  list 
#  2. Func random choice for homework list
#  3. Input names family 
#  4. print result
import random

working_home_list = ["Cooking", "Vacuum the apartment", "Wash the dishes",
                     "Water  the flower", "To wash the floor", "Learn English",
                     "Read the book", "Go in for sport"]


family_list = input("What is name your family?\n").split(", ")

print(family_list)
count_family = len(family_list)
print(count_family)

for work in range(count_family):
    random_work = random.choice(working_home_list)
    print(family_list[work] + ": " + random_work)












# #  Імпортуємо функцію рандом
# import random
# # Створюємо список завдань
# working_home_list = ["Cooking", "Vacuum the apartment",
#                      "Wash the dishes", "Water the flowers", 
#                      "To wash the floor", "Learn English",
#                      "Read the book", "Go in for sport"]


# family_list = list(input("What is name your family? \n").split(", ")) # Створюємо список і розділяємо його комами
# count_family = len(family_list) # рахуємо кількість імен в родині

# print()

# # створюємо цикл індексів родини 
# for work in range(count_family): # Цикл проходить по всіх іменах родини
#     # вибираємо випадкову задачу
#     random_work = random.choice(working_home_list)
#     # Друкуємо результат 
#     print(family_list[work] + ": " + random_work)
#     #family_list[work] == ім'я члена сім'ї[домашня справа]