

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

flag = True
while flag:
    action = input("What is your action? ")
    
    if action == "exit":
        flag = False
    else:
        
        num1 = int(input("What is first number? "))
        num2 = int(input("What is second number? "))
        
        if action == "+":
            print(f"{num1} + {num2} = {add(num1, num2)}")
            
        elif action == "-":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
        elif action == "*":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
        elif action == "/":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
