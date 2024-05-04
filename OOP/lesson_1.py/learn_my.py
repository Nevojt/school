#  Attribute classes

# class Car:
#     # wheels_number = 4
#     def __init__(self, name: str, color: str, year: int, is_crashed: bool) -> None:
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         self.wheels_number = 4
        
        
#     def drive(self, city: str):
#         print(f"Car {self.name} is driving to {city}")
        
#     def change_color(self, new_color: str):
#         self.color = new_color
        
  
# opel_car = Car("Opel", "blue", 1999, True)
# opel_car.drive("London")
# opel_car.change_color("Red")
# print(opel_car.color)

# mazda_car = Car("Mazda", "blue", 1999, True)
# mazda_car.drive("Paris")
# mazda_car.change_color("Yellow")
# print(mazda_car.color)
        
# mazda_car = Car(name="Mazda", color="yellow", year=2018, is_crashed=True)

# print(mazda_car.name)
# print(mazda_car.color)
# print(mazda_car.year)
# print(mazda_car.is_crashed)

# bmw_car = Car(name="BMW", color="black", year=2018, is_crashed=False)
# print(bmw_car.name)
# print(bmw_car.color)
# print(bmw_car.year)
# print(bmw_car.wheels_number)

# number_of_3_cars = Car.wheels_number * 3
# print(number_of_3_cars)


# class Circle:
#     pi = 3.14
    
#     def __init__(self, radius: int = 1) -> None:
#         self.radius = radius
#         self.circumference = 2 * self.pi * self.radius
        
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
    
#     def get_circumference(self):
#         return 2 * self.pi * self.radius
    

# circle_1 = Circle(radius=5)
# circle_2 = Circle(radius=30)
# circle_3 = Circle()

# print(circle_3.radius)

# print(circle_1.circumference)

# print(circle_1.get_area())
# print(circle_1.get_circumference())
 
# print(circle_2.get_area())
# print(circle_2.get_circumference())



class Item:
    
    pay_rate = 0.8
    def __init__(self, name: str, price: int, quantity: int = 0) -> None:
        assert price >= 0, f"Price {price} is not greater that zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
        
        
        self.price = price
        self.name = name
        self.quantity = quantity
        
    # def calculated_total_price(self, x, y):
    #     return x * y   
    
    def calculated_total_price(self):
        return self.price * self.quantity
        
item_1 = Item("iPhone", 100, -5)
item_2 = Item("Laptop", 1000, 3)

print(item_2.name)

        
# print(item_1.calculated_total_price(item_1.price, item_1.quantity))
print(item_1.calculated_total_price())
# print(item_2.calculated_total_price())