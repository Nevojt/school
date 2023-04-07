import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic_code():
    user_input = input("What is word NATO?: ").upper()
    try:
        nato_list = [dictionary[letter] for letter in user_input]       
    except KeyError:
        print("Sorry, only letters the alphabet please.")
        generate_phonetic_code()
    else:
        print(nato_list)
        
generate_phonetic_code()
