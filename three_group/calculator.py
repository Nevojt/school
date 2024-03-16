
print("Hello, I am difficult calculator!")
# Беремо перше число
first_number = int(input("First number\n"))
#  Беремо друге число 
second_number = int(input("Second number\n"))
symbol = input("What to do about is?\n +, -, *, /\n")

if symbol == "+":
    result = first_number + second_number
    print(result)
    
elif symbol == "-":
    result = first_number - second_number
    print(result)