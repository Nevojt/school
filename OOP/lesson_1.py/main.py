

class Dog:
    def __init__(self, name: str, age: int, voice: bool):
        self.name = name
        self.age = age
        self.voice = voice
        
    def get_name(self):
        return self.name
    
    def set_age(self, age: int):
        self.age = age
    
    



dog_1 = Dog("Tigre", 12, True)
dog_2 = Dog("Puma", 34, False)

# print(dog_1.name)
print(dog_1.get_name())
print(dog_1.age)
dog_1.set_age(38)
print(dog_1.age)

print(dog_1.voice)

# print(dog_2.name)




















# #  Blueprint
# class Dog:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         # print(name)
        
        
#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
#     def set_age(self, age: int):
#         self.age = age
        
#     # def plus_one(self, x):
#     #     return x + 1
    
#     # def bark(self):
#     #     print("Woof!")
        
        
        
        
# # d = Dog()
# # d.bark()
# # print(d.plus_one(2))

# # print(type(d))

# d = Dog("Tiger", 12)
# # print(d.name)
# # print(d.age)
# d.set_age(22)
# print(d.get_name())
# print(d.get_age())

# d2 = Dog("Bill", 5)
# # print(d2.name)
# # print(d2.age)
# print(d2.get_name())
# print(d2.get_age())