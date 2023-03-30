import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is word NATO?: ").upper()
nato_list = []
            
[nato_list.append(value) for letter in user_input for (key, value) in dictionary.items() if letter == key]       
            
print(nato_list)
