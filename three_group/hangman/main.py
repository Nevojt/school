
import random
from hungman_words import list_string_ukr
from hungman_art import logo, stages

print(logo)

letters = random.choice(list_string_ukr)
lives = 6
letter_list = []

for let in letters:
    letter_list.append(let)
    blank = len(letter_list) * ['_']

print(blank)

flag = False
while not flag:
    out_play = input("Яку літеру ти вибереш?\n").lower()
    len_letter_list = len(letter_list)
    
    for play in range(len_letter_list):
        new_letter = letter_list[play]
        if out_play == new_letter:
            blank[play] = new_letter
            print("Ти вгадав літеру!!!")
    
    if out_play not in letters:
        print(f"Букви {out_play} немає в цьому слові. Ти втратив життя((()))")
        lives -= 1
        print(stages[lives])

    print(blank)
    
    if '_' not in blank:
        flag = True
        print("Ти вгадав слово!!")
        
    if lives == 0:
        flag = True
        print("Ти програв!!!")


