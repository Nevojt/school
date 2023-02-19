from art import logo
from random import randint
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0  
def check_answer(guess_user, number, turns):
    if guess_user > number:
        print("Too high")
        print("Guess again.")
        return turns -1
    elif guess_user < number:
        print("Too low.")
        print("Guess again.")
        return turns -1
    else:
        print(f"You got it! The answer was {number}")
        
def set_difficulty():
    choise_user = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    
    if choise_user == "easy":
        return EASY_LEVEL_TURNS           
    elif choise_user == "hard":
        return HARD_LEVEL_TURNS
        
def game():
    print("Welcome to the Number Guessung Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    # print(f"Pssst, the correct answer is {number}")
    
    turns = set_difficulty()
    
    guess_user = 0
    while guess_user != number:
        print(f"You have {turns} attempts remaining to guess the number")
        guess_user = int(input("Make a guess:  "))

        turns = check_answer(guess_user, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
            
game()