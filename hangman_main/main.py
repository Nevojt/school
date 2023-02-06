import random
from hangman_words import list_string
from hangman_art import logo, stages

print(logo)
letters = random.choice(list_string)
lives = 6
letter_list = []
for let in letters:
    letter_list.append(let)
    blank = len(letter_list) * ['_']
print(blank)

flag = False
while not flag:
    out_play = input("what is leter?\n").lower()
    len_leter_list = len(letter_list)

    for play in range(len_leter_list):
        new_letter = letters[play]
        if out_play == new_letter:
                blank[play] = new_letter
                print("You've already guessed!")
    if out_play not in letters:
      print(f"You guessed {out_play} that's not in the word. You lose a live.")
      lives -= 1
      print(stages[lives])
        
    print(blank)
    
    if '_' not in blank:
        flag = True
        print("You win")
    if lives == 0:
        flag = True
        print('You lose!')
    