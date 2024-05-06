

class Car:
    
    def __init__(self, name: str, color: str, year: int,
                 is_crashed: bool, price: int) -> None:
        self.name = name
        self.color = color
        self.year = year
        self.wheels = 4
        self.is_crashed = is_crashed
        self.price = price
        
    def change_color(self, new_color: str):
        self.color = new_color
        
    def change_crashed(self, crashed: bool):
        self.is_crashed = crashed
        
    def later_price(self, crashed: bool):
        if self.is_crashed == True:
            return self.price * 0.2
        else:
            self.price
            


car_1 = Car("BMW M1", "Black", 2010, True, 5000)
car_2 = Car("Alfa Romeo", "Yellow", 2000, False, 7000)

# print(car_1.color)
car_1.change_color("Red")
print(car_1.color)
# car_1.change_crashed(False)
print(car_1.is_crashed)

car_1.later_price()
print(car_1.price)
