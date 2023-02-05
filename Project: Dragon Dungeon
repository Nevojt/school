print('''
*******************************************************************************
                                       ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###' -Tua Xiong     .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""' 
*******************************************************************************
''')
print("Welcome to Dragon Dungeon.")
print("Your adventure begins!!!") 
print("You light a torch and see three caves...")

#Write your code below this line 👇
healt = 0
potion_fire = 0
caves = input("Select a drection: Left, Direct or Right?\n")

if caves == "Direct":
    print("You met Troll")
    run_hero = input("You run Left, Right or Hide?\n")
    if run_hero == "Left":
        print("You attack Troll!!")
        attack_left = input("Torch or Sword?\n")
        if attack_left == "Torch":
            healt += 1
            print("You scared the Troll, he runs awey")
        else:
            print("You pissed off a Troll, you're a moron")
            print("Game Over.")
    elif run_hero == "Right":
        print("You attack Troll!!")
        attack_right = input("Torch or Sword?\n")
        if attack_right == "Sword":
            healt += 1
            print("You hurt the Troll, he runs away.")
        else:
            print("You torch goes out and you die at the troll's clutches!")
            print("Game Over")
    else:
        print("You hide behind a rock, a Troll finds you by the light of a torch and tears you to pieces!")
        print("Game Over.")
elif caves == "Right":
    print("You meet a Wizard, he offers you a magic potion.")
    wizard_potion = input("Yes or No?\n")
    if wizard_potion == "No":
        healt += 1
        potion_fire += 1
        print("You get a protection potion and move on.")
    else:
        print("You drink the potion and die from the poison.")
        print("Game Over.")
else:
    print("There is an abyss ahead and you will fall anto it.")

if healt >= 1:
    print("In front of you at the door")
    door = input("Which charm do you have? 'Red', 'Yellow' or  'White\n")
    if door == "Red":
        print("You see a chest.")
        chest = input("Open the chest?   Yes or No\n")
        if chest == "Yes":
            print("You open the chest, it disappears. A spiked ceiling falls from the mountain.")
            print("You dead")
            print("Game Over.")
        else:
            print("You go into the light and disappear.")
            print("Opend your eyes, you see that you are on the top of the mountain with.")
            print("A box of gold in your hands.")
            print("You are a Winner.")
    elif door == "White":
        print("You found the dragon!!!")
        print("The dragon attacks with fire!")
        if potion_fire >= 1:
            print("The potion worked!")
            print("You counterattack worked, the dragon is dead!")
            print("You have gained fame and fortune!")
        else:
            print("Your body burns, yuo die...")
    else:
        print("You are trapped, locked up forever...")
        print("Game Over.")

else:
    print("You are dead!")
