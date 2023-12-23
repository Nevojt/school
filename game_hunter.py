print("Hello new warrior!!!")
print("Правила гри!")
print("Ти можеш ходити в право 'right' та ліво 'left' ")

print("Start game!!!")
print("")
print("Перед тобою дві двері: ліва та права.")
print("Яку ти вибереш?")

walk = input().lower()

if walk == "RIGHT":
    print("Ти вмер АХАХААХА")
    
    
elif walk == "LEFT":
    print("Ти знайшов кристал!")
    print("Підняти чи ні?")
    
    gams = input("Yes or No?\n").lower()
    if gams == "Yes":
        print("Ти отримав кристал.")
        print("Цей кристал був Огра і він тебе помітив.")
        
        battle = input("Тікати чи битись?\n Yes or No?").lower()
        
        if battle == "Yes":
            print("Огр дає тобі підсрачник і ти вилетів з печеру")
            print("Game Over")
            
        elif battle == "No":
            print("Огр тебе наздоганяє.")
            print("Game Over")
        else:
            print("Bad input.")
        
        
    elif gams == "No":
        print("Йдеш далі...")
        print("Ти побачив дві двері. В яку зайдеш?")
        
        door = input("В яку зайдеш? Left or Right\n").lower()
        if door == "left":
            print("За дверима була пастка в яку ти потрапив")
            print("Game Over")
            
        elif door == "right":
            print("За дверима ти знайшов принцесу.")
        else:
            print("Bad input.")
            
    else:
        print("Bad input.")
            
else:
    print("Bad input.")
            
        
        
        
        








