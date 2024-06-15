# from math import pi
# # def test():
# #     return "test"
    
    
# # print(test())

# def one_argument(a):
#     return a

# one = one_argument(pi)
# # print(one)

# def two_argument(a, b):
#     return [a + b,  b + a]

# two = two_argument("Hello ", "Word")
# # two.reverse()
# print(two[::-1])

def three_argument(age: int, age2: int, name: str):
    """
    age: int Age user
    age2: int Age minimum
    name: str Name user
    """
    multy = age_multiply(age2)

    if age < multy:
        print("Your yong hand ", name, multy)
    elif age == multy:
        print("Your Lacked hand,  ", multy)
    else:
        print(f"Welcome Club {name}", multy)

def age_multiply(age: int):
    return age * 2


three_argument(age=12, age2=18, name="Youra")
# three_argument(age=134, age2=18, name="Artem")
# age_user = int(input("What is your age? "))
# name_user = input("What is your name? ")
# three_argument(age=age_user, age2=18, name=name_user)


