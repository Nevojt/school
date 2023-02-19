from art import logo
import random
print(logo)
print("Welcome to the Number Guessung Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

print(f"Pssst, the correct answer is {number}")

choise_user = input("Choose a difficulty. Type 'easy' or 'hard': \n")
healt_user = 0

if choise_user == "easy":
    healt_user = 10
        
elif choise_user == "hard":
    healt_user = 5
# print(f"You have {healt_user} attempts remaining to guess the number")



flag = True
while flag:
    print(f"You have {healt_user} attempts remaining to guess the number")
    guess_user = int(input("Make a guess:  "))
    if guess_user == number:
        print(f"You got it! The answer was {number}")
        flag = False
    if healt_user == 1:
        print("You've run out of guesses, you lose.")
        flag = False
    elif guess_user > number:
        healt_user -= 1
        print("Too high")
        print("Guess again.")
    elif guess_user < number:
        healt_user -= 1
        print("Too low.")
        print("Guess again.")