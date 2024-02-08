# from info_her import races_in_games, character_classes, weapons_list
# import random

# #  Created boss
# boss_races = random.choice(races_in_games)
# boss_character = random.choice(character_classes)
# boss_weapon = random.choice(weapons_list)

# boss_heal = races_in_games.index(boss_races) + character_classes.index(boss_character) + random.randint(10, 100)
# boss_damage = weapons_list.index(boss_weapon) + character_classes.index(boss_character) + random.randint(1, 10)

# # Created user
# user_races = random.choice(races_in_games)
# user_character = random.choice(character_classes)
# user_weapon = random.choice(weapons_list)

# user_heal = races_in_games.index(user_races) + character_classes.index(user_character) + random.randint(10, 100)
# user_damage = weapons_list.index(user_weapon) + character_classes.index(user_character) + random.randint(1, 10)

# print(f"User personage: {user_races}, {user_character}, {user_weapon}")
# print(f"User heal: {user_heal}")
# print(f"User damage: {user_damage}")



# user_brok = user_heal - boss_damage
# boss_brok = boss_heal - user_damage

# print(f"User heal: {user_brok}")
# print(f"Boss heal: {boss_brok}")

#  ========== First Group ==========

from info_her import races_in_games, character_classes, weapons_list
import random

# boss = f"{random.choice(races_in_games)} {random.choice(character_classes)} {random.choice(weapons_list)}"

boss_race = random.choice(races_in_games)
boss_character = random.choice(character_classes)
boss_weapon = random.choice(weapons_list)


print(f"Boss race: {boss_race}")
print(f"Boss character: {boss_character}")
print(f"Boss weapon: {boss_weapon}")


hp_boss_r = races_in_games.index(boss_race)
hp_boss_c = character_classes.index(boss_character)
damage_boss = weapons_list.index(boss_weapon)

full_hp_boss = hp_boss_r + hp_boss_c + random.randint(1, 100)

if full_hp_boss < 50:
    full_hp_boss += random.randint(30, 100)

full_damage = hp_boss_c + damage_boss + random.randint(1, 100)

# print(hp_boss_r)
# print(hp_boss_c)
print(f"Full HP Boss: {full_hp_boss}")
print(f"Full Damage Boss: {full_damage}")

















#  ========== Second Group ==========

from info_her import races_in_games, character_classes, weapons_list
import random

# Crated Boss 

boss_race = random.choice(races_in_games)
boss_character = random.choice(character_classes)
boss_weapon = random.choice(weapons_list)

print(f"Boss rase: {boss_race}")
print(f"Boss character: {boss_character}")
print(f"Boss weapon: {boss_weapon}")

boss_hp_r = races_in_games.index(boss_race)
boss_hp_c = character_classes.index(boss_character)
damage_weapon_boss = weapons_list.index(boss_weapon)

full_hp_boss = boss_hp_r + boss_hp_c + random.randint(1, 100)
full_damage_boss = damage_weapon_boss + boss_hp_c + random.randint(1, 100)

if full_hp_boss < 50:
    full_hp_boss = 50
    
full_hp_boss += random.randint(30, 100)

print(f"Full HP Boss: {full_hp_boss}")
print(f"Full Damage Boss: {full_damage_boss}")

# Created User
user_race = ...
user_character = ...
user_weapon = ...



