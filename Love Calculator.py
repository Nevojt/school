print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()
name_true = 0
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
name_true += t + r + u + e

name_love = 0
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
name_love += l + o + v + e

love_int = int(str(name_true) + str(name_love))

if love_int < 10 or love_int > 90:
    print(f"Your score is {love_int}, you go together like coke and mentos.")
elif love_int >= 40 and love_int <= 50:
    print(f"Your score is {love_int}, you are alright together.")
else:
    print(f"Your score is {love_int}.")
