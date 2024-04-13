print("Hello new player!")
print("This is game dangerous Dragons!!!")
name =  input("What's your name?\n")

print("You joined the cave and see three door ")

choice_door = int(input("Which door do you want to open?\n 1 or 2 or 3\n"))
if choice_door == 1:
    print("You wear attack Zmej Gorinich")
    print("You DEAD!!!!")
    
elif choice_door == 2:
    print("You see Yura")
    battle = input("Attack or run!!\n")
    if battle == "attack":
        print("Youra give you a hard trindula")
        print("You shit")
    elif battle == "run":
        print("Yora tobi dav pid sraku")
        print("You flight to the Star!!!")
        
elif choice_door == 3:
    print("You see 2 chest")
    open_chest = input("Open or No?\n")
    if open_chest == "open":
        choice_chest = int(input("1 or 2"))
        if choice_chest == 1:
            print("You have dulka z makom AHAHAHAHHAHAHAHA")
        elif choice_chest == 2:
            print("You meet Yora")
            print("Yora dav tobi smachniy podsrachik")
            print("You cry and you little girl")
    elif open_chest == "no":
        print("Yora run to you and open your ass!!!")
    