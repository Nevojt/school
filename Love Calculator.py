# # print("Welcome to the Love Calculator!")
# # name1 = input("What is your name? \n")
# # name2 = input("What is their name? \n")

# # name = name1.lower() + name2.lower()
# # name_true = 0
# # t = name.count('t')
# # r = name.count('r')
# # u = name.count('u')
# # e = name.count('e')
# # name_true += t + r + u + e

# # name_love = 0
# # l = name.count('l')
# # o = name.count('o')
# # v = name.count('v')
# # e = name.count('e')
# # name_love += l + o + v + e

# # love_int = int(str(name_true) + str(name_love))

# # if love_int < 10 or love_int > 90:
# #     print(f"Your score is {love_int}, you go together like coke and mentos.")
# # elif love_int >= 40 and love_int <= 50:
# #     print(f"Your score is {love_int}, you are alright together.")
# # else:
# #     print(f"Your score is {love_int}.")




# print("Hello i'm calculator love")

# name_1 = input("First name:\n")
# name_2 = input("Second name:\n")

# name_3 = (name_1 + name_2).lower()

# # print(name_3)
# # count_name = name_3.count("affff")
# # print(count_name)

# t = name_3.count("t")
# r = name_3.count("r")
# u = name_3.count("u")
# e = name_3.count("e")

# true = str(t + r + u + e)

# l = name_3.count("l")
# o = name_3.count("o")
# v = name_3.count("v")
# e = name_3.count("e")

# love = str(l + o + v + e)

# result = int(true + love)

# if result < 10:
#     print("Not loves.....")
    
# elif result >= 11 or result <= 90:
#     print("True love.")
    
# else:
#     print("Super  love...")






print("Welcome to Love Calculator!!!")

name_1 = input("First name:\n")
name_2 = input("Second name:\n")

name_3 = (name_1 + name_2).lower()

t = name_3.count("t")
r = name_3.count("r")
u = name_3.count("u")
e = name_3.count("e")

true = str(t + r + u + e)

l = name_3.count("l")
o = name_3.count("o")
v = name_3.count("v")
e = name_3.count("e")

love = str(l + o + v + e)

result = int(true + love)
print(result)

if result < 10:
    print("Sorry this is not love...")
    
elif result >= 11 or result <= 90:
    print("This is true love!!!!")
    
else:
    print("This is SUPER LOVE!!!!!!!")










