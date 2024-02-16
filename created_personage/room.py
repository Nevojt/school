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

# TODO:
# 1. Boss defend
# 2. Boss counterattack % attack
# 3. Boss dodged

print()
while True:
    choose = input("Choose Attack or Defend or Dodged: A or D or G?\n")
    # User attack
    if choose == "A":
        # random choose 
        user_attack = randint(0, 2)
        
        # full attack user
        if user_attack == 0:
            hp_boss -= damage_user
            print("Full attack user 💪")
             
        # Block user attack + 25 % HP boss
        elif user_attack == 1:
            hp_boss -= damage_user - int(damage_user * 0.25)
            print("Boss blocked 25% of your attack 😭")
            
        #  Dodged user attack + from 10 HP to full attack user
        elif user_attack == 2:
            hp_boss -= damage_user - (hp_boss + randint(10, damage_user))
            print("Boss dodger your attack 😩")
            
        #  if HP boss is 0 stop game
        if hp_boss <= 0:
            print("You Win! 🤩🤩🤩")
            break
     
    #  User defend + 25% HP
    elif choose == "D":
        hp_user += int(hp_user * 0.25)
    
    #  User dodged + from 10 HP to full attack boss
    elif choose == "G":
        hp_user += randint(10, damage_boss)       

    # Attack Boss
    print()
    print(f"The boss attacks 😈😈 the user for {damage_boss} HP\n")
    hp_user = hp_user - damage_boss
    if hp_user <= 0:
        print("You have died! 💀")
        break
    
    
    
    print(f"HP User 👀: {hp_user}")
    print(f"HP Boss 😈: {hp_boss}")