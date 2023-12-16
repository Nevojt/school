print("Hello gamer!!!")
print("Перед тобою дві двері яку ти вибереш?")

walk = input("Left or Right?\n").lower()

if walk == "left":
    print("Ти зустрів Огра").upper()
    
    battle = input("Тікати чи битись?\n Yes or No?").lower()
    if battle == "yes":
        print("Двері зачинені, тікати нікуди")
        print("Огр дає тобі квіти.")
        
        do = input("Взяти квіти?\nYes or No").lower()
        if do == "yes":
            print("Він каже зробити вінок.")
            
            winok = input("Yes or No").lower()
            if winok == "yes":
                print("")
                
            elif winok == "no":
                print("Огр б'є нас квітами по сраці!!!")
            
            
        elif do == "no":
            print("Огр плаче.")
        
        
        
    elif battle == "no":
        print("Ти налякав Огра і він втікає.").upper()
    
    
    
    
    
    
    
elif walk == "right":
    print("За дверима ти побачив скриньку.")