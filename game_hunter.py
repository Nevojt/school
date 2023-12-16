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
            print("")
            
        elif battle == "No":
            print("")
        
        
    elif gams == "No":
        print("Йдеш далі...")








