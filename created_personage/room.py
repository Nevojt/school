from random import randint, uniform
from main import boss, user

boss_all = boss()
boss_hp = boss_all[0]

user_all = user()
user_hp = user_all[0]

print(boss_hp)
print()

print(user_hp)


while True:
    boss_damage = boss_all[1]
    user_damage = user_all[1]
    
    choose = input("Choose \nA -> Attack\nD -> Defend\nG -> Dodge\n-> ").lower()
    # Attack for user
    if choose == "a":
        boss_hp -= user_damage
        print(f"Boss HP {boss_hp}")
        if boss_hp <= 0:
            print("You Won!")
            break
        
    elif choose == "d":
        boss_damage -= boss_damage * 0.3
        
    elif choose == "g":
        boss_damage -= randint(10, boss_damage)
        boss_hp -= user_damage * uniform(0.3, 0.8)
        print(f"Boss HP {boss_hp}")
        if boss_hp <= 0:
            print("You Won!")
            break
        
        
        
    
    else: 
        print("Bad choose")   
        
    # Attack Boss
    choose_boss = randint(0,2)
    
    if choose_boss == 0:
        print("attack")
        user_hp -= boss_damage
        if user_hp <= 0:
            print("You died")
            break
        
    elif choose_boss == 1:
        print("defend")
        boss_hp += user_damage * 0.3
        if user_hp <= 0:
            print("You Bad !")
            break
        
    elif choose_boss == 2:
        print("dodge")
        boss_hp += randint(10, user_damage)
        user_hp -= boss_damage * uniform(0.3, 0.8)
        if user_hp <= 0:
            print("You Lose!")
            break
        
















# # # second
# from main import boss, user
# from random import randint, uniform


# boss_all = boss()
# boss_hp = boss_all[0]
# # boss_damage = boss_all[1]

# user_all = user()
# user_hp = user_all[0]
# # user_damage = user_all[1]

# print()
# # Attack User
# while True:
#     boss_damage = boss_all[1] # Оновлення Damage boss кожен раз при початку циклу
#     user_damage = user_all[1] # Оновлення Damage user кожен раз при початку циклу
    
#     choose = input("Choose\n-> A == Attack\n-> D == Defend\n-> G == Dodge\n-> ").lower()
#     if choose == "a":
#         boss_hp -= user_damage
#         if boss_hp <= 0:
#             print("You Won!")
#             break
    
#     elif choose == "d":
#         boss_damage -= boss_damage * 0.3
        
#     elif choose == "g":
#         boss_damage -= randint(10, boss_damage)
#         boss_hp -= user_damage * uniform(0.3, 0.8)
#         if boss_hp <= 0:
#             print("You Won!")
#             break
#     else:
#         print("Bad choice!")
        
    

# # Attack Boss
#     choose_boss = randint(0,2)
    
#     if choose_boss == 0:
#         print("attack")
#         user_hp -= boss_damage
#         if user_hp <= 0:
#             print("You died")
#             break
        
#     elif choose_boss == 1:
#         print("defend")
#         boss_hp += user_damage * 0.3
#         if user_hp <= 0:
#             print("You Bad !")
#             break
        
#     elif choose_boss == 2:
#         print("dodge")
#         boss_hp += randint(10, user_damage)
#         user_hp -= boss_damage * uniform(0.3, 0.8)
#         if user_hp <= 0:
#             print("You Lose!")
#             break
    
    
#     print(f"HP Boss: {boss_hp}")  
#     print(f"DefendingBoss: {boss_damage}")
#     print(f"HP User: {user_hp}")
#     print()































# boss_all = boss()
# hp_boss = boss_all[0]
# damage_boss = boss_all[1]
# # print(hp_boss)
# # print(damage_boss)

# user_all = user()
# hp_user = user_all[0]
# damage_user = user_all[1]
# # print(hp_user)
# # print(damage_user)

# # TODO:
# # 1. Boss defend
# # 2. Boss counterattack % attack
# # 3. Boss dodged

# print()
# while True:
#     choose = input("Choose Attack or Defend or Dodged: A or D or G?\n")
#     # User attack
#     if choose == "A":
#         # random choose 
#         user_attack = randint(0, 2)
        
#         # full attack user
#         if user_attack == 0:
#             hp_boss -= damage_user
#             print("Full attack user 💪")
             
#         # Block user attack + 25 % HP boss
#         elif user_attack == 1:
#             hp_boss -= damage_user - int(damage_user * 0.25)
#             print("Boss blocked 25% of your attack 😭")
            
#         #  Dodged user attack + from 10 HP to full attack user
#         elif user_attack == 2:
#             hp_boss -= damage_user - (hp_boss + randint(10, damage_user))
#             print("Boss dodger your attack 😩")
            
#         #  if HP boss is 0 stop game
#         if hp_boss <= 0:
#             print("You Win! 🤩🤩🤩")
#             break
     
#     #  User defend + 25% HP
#     elif choose == "D":
#         hp_user += int(hp_user * 0.25)
    
#     #  User dodged + from 10 HP to full attack boss
#     elif choose == "G":
#         hp_user += randint(10, damage_boss)       

#     # Attack Boss
#     print()
#     print(f"The boss attacks 😈😈 the user for {damage_boss} HP\n")
#     hp_user = hp_user - damage_boss
#     if hp_user <= 0:
#         print("You have died! 💀")
#         break
    
    
    
#     print(f"HP User 👀: {hp_user}")
#     print(f"HP Boss 😈: {hp_boss}")