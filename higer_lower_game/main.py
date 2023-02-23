from game_data import data
from art import logo, vs
from random import choice
import os
clear = lambda: os.system('cls')

def get_random_account():
    """Get data from random account"""
    return choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and return True if they got it right.
    Or False it they got it wrong.

    Args:
        guess (_type_): input users
        a_followers (_type_): followers_count A
        b_followers (_type_): followers_count B
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
    
def game():
    print(logo)
    score = 0
    flag = True
    account_a = get_random_account()
    account_b = get_random_account()
    
    while flag:
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()
            print(f"Compare A: {format_data(account_a)}.")
            print(vs)
            print(f"Against B: {format_data(account_b)}.")
            
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_followers_count = account_a["follower_count"]
            b_followers_count = account_b["follower_count"]
            
            is_correct = check_answer(guess, a_followers_count, b_followers_count)
            
            clear()
            print(logo)
            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                flag = False
                print(f"Sorry, that's wrong. Final score: {score}")
                
game()
            


