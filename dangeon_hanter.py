print("Hello gamer!!!")
print("Перед тобою дві двері яку ти вибереш?")

walk = input("Left or Right?\n").lower()

if walk == "left":
    print("Ти зустрів Огра")
    
    battle = input("Тікати чи битись?\n Yes or No?").lower()
    if battle == "yes":
        print("Двері зачинені, тікати нікуди")
        print("Огр дає тобі квіти.")
        
        do = input("Взяти квіти?\nYes or No").lower()
        if do == "yes":
            print("Він каже зробити вінок.")
            
            winok = input("Yes or No\n").lower()
            if winok == "yes":
                print("Огр на тобі одружується, проти твоєї волі!!!")
                
            elif winok == "no":
                print("Огр б'є нас квітами по сраці!!!")
                
            else:
                print("Bad input")
            
            
        elif do == "no":
            print("Огр плаче.")
            
        else:
            print("Bad input")
        
        
        
    elif battle == "no":
        print("Ти налякав Огра і він втікає.")
        
    else:
        print("Bad input")
    
    
    
elif walk == "right":
    print("За дверима ти побачив скриньку.")
    box = input("Відкрити чи ні. Yes or No ").lower()
    
    if box == "Yes":
        print("З неї вилазить Аня.")
        print("І затягує тебе в середину")
        
        print("Аня каже тобі\n-Допоможи мені будь ласка")
        
        
        need_anna = input("Yes or No")
        
        if need_anna == "Yes":
            print("")
            
        elif need_anna == "No":
            print("")
            
            
    
    elif box == "No":
        print()
        
    else:
        print("Bad input")
    
        
    
    
else:
    print("Bad input")