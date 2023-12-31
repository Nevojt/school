import random

def play_game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.(___)
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
    ---.(___)
    '''
    
    game_images = [rock, paper, scissors]

    name = input("What's your name? ")
    print("Welcome to the game, " + name + "!")

    while True:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice >= 3 or user_choice < 0:
            print("Invalid number, you lost!")
            continue

        print(game_images[user_choice])

        bot_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[bot_choice])

        if user_choice == 0 and bot_choice == 2:
            print("You win!")
        elif bot_choice == 0 and user_choice == 2:
            print("You lose")
        elif bot_choice > user_choice:
            print("You lose")
        elif user_choice > bot_choice:
            print("You win!")
        elif user_choice == bot_choice:
            print("It's a draw")

        play_again = input("Do you want to play another round? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing, " + name + "!")

play_game()