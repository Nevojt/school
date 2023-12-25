import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_list = random.randint(0, len(names))
name_cash = names[name_list] 
print(f"{name_cash} is going to buy the meal today!")
