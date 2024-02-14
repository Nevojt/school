# from main import boss, user

# boss()
# user()










from main import boss, user
from random import randint
# boss()
# user()

# def hello():
#     return "Hello"

# def func(a, b):
#     hello1 = hello()
#     c = (a + b) * hello1
#     return c

# print(func(2, 4))
# print(func(randint(1, 100), randint(1, 100)))
# print(func(randint(1, 100), 5))
# print(func("Hello ", "world"))

# result = func(randint(1, 100), randint(1, 100))
# hello = func("Hello ", "world.")

# count = result * f"\n{hello}"
# print(count)
# len_count = count.split(".")
# print(len_count)
# print(len(count))
# print(len(len_count))























boss_all = boss()
hp_boss = boss_all[0]
damage_boss = boss_all[1]
# print(hp_boss)
# print(damage_boss)

user_all = user()
hp_user = user_all[0]
damage_user = user_all[1]
# print(hp_user)
# print(damage_user)

print()
while True:
    choose = input("Choose Attack or Defend: A or D? ")
    if choose == "A":
    # Attack User
        hp_boss = hp_boss - damage_user
        if hp_boss <= 0:
            print("You Vin!")
            break
        
    elif choose == "D":
        hp_user += int(hp_user * 0.25)
        

    # Attack Boss
    print()
    hp_user = hp_user - damage_boss
    if hp_user <= 0:
        print("You have died!")
        break
    print(f"HP User: {hp_user}")
    print(f"HP Boss: {hp_boss}")