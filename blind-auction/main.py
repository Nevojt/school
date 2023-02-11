import os
from logo import logo
clear = lambda: os.system('cls')
print(logo)


list_humans = []
flag = True
while flag:  

  name = input("What is your name?  ")
  count = int(input("What is your bid?  $"))  
  humans = input("Are there any other bidders? Type  'yes or no?'  ").lower()

  if humans == "no":
    flag = False
    auction(name, count)
  elif humans == "yes":
    flag = True
    clear()

  def auction(key, value):
    dict_list = {key: value}
    list_humans.append(dict_list)
    
    highest_bid = 0
    winner = ''
    for keys in list_humans:
        for k in keys:
            max_count = keys[k]
            if max_count > highest_bid:
                highest_bid = max_count
                winner = k
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

  





    
    