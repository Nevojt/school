from info_her import races_in_games, character_classes, weapons_list
import random

#  Created boss
boss_races = random.choice(races_in_games)
boss_character = random.choice(character_classes)
boss_weapon = random.choice(weapons_list)

boss_heal = races_in_games.index(boss_races) + character_classes.index(boss_character) + random.randint(10, 100)
boss_damage = weapons_list.index(boss_weapon) + character_classes.index(boss_character) + random.randint(1, 10)

# Created user
user_races = random.choice(races_in_games)
user_character = random.choice(character_classes)
user_weapon = random.choice(weapons_list)

user_heal = races_in_games.index(user_races) + character_classes.index(user_character) + random.randint(10, 100)
user_damage = weapons_list.index(user_weapon) + character_classes.index(user_character) + random.randint(1, 10)

print(f"User personage: {user_races}, {user_character}, {user_weapon}")
print(f"User heal: {user_heal}")
print(f"User damage: {user_damage}")



user_brok = user_heal - boss_damage
boss_brok = boss_heal - user_damage

print(f"User heal: {user_brok}")
print(f"Boss heal: {boss_brok}")
