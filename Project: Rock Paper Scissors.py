rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Імпортуємо модуль рандом із бібліотеки Python
import random

# Присвоєння змінній функцію рандомізації
bot = random.randint(0, 2)  # Ця функція визначає випадкове число від 0-2

print("Welcome to game ROCK, PAPER, SCISSORS!!!!")

user = int(input("What do you choose? Type 0 Rock, 1 Paper, 2 Scissors:\n"))

# Всі цифри які більшу або менше зазначеного діапазону.
if user >= 3 or user < 0:
  print("You lose the game!!!")

# Обробляємо основний функціонал
elif bot == 0 and user == 1:
  print("Bot\n", rock)
  print("You\n", paper)
  print("You WIN!!!")

elif bot == 0 and user == 2:
  print("Bot\n", rock)
  print("You\n", scissors)
  print("You lose!!!")
  
elif bot == 1 and user == 0:
  print("Bot\n", paper)
  print("You\n", rock)
  print("You lose!!!")
  
elif bot == 1 and user == 2:
  print("Bot\n", paper)
  print("You\n", scissors)
  print("You WIN!!!")
  
elif bot == 2 and user == 0:
  print("Bot\n", scissors)
  print("You\n", rock)
  print("You WIN!!!")
  
elif bot == 2 and user == 1:
  print("Bot\n", scissors)
  print("You\n", paper)
  print("You lose!!!")

# Всф інші випадки
else:
  print("You lose the game!!!")



