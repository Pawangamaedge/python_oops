from abc import ABC, abstractmethod

class Shape(ABC):

     @abstractmethod 
     def area(self):
          pass
     
     @staticmethod
     def description():  # this can be callable outside the class because this is staticmethod 
          print("this is shape description")

class Rectangle(Shape):
     def __init__(self, width, height):
          self.width = width
          self.height = height

     def area(self):
          return self.width * self.height
     
     @staticmethod
     def description():
          print("this is rectangle description")

class Circle(Shape):
     def __init__(self, radius, pi = 3.14):
          self.radius = radius
          self.pi = pi
     
     def area(self):
          return self.pi * self.radius ** 2

     @staticmethod
     def description():
          print("this is circle description")

# rectangle = Rectangle(20, 2)
# rectangle.description()
# print(f"rectangle area is: {rectangle.area()}")

# circle = Circle(4)
# circle.description()
# print(f"circle area is: {circle.area()}")

# Shape.description()


class Car:
     total_car = 0
     def __init__(self, car_name):
          self.car_name = car_name
          Car.total_car+=1

     @classmethod
     def get_total_car(cls):
          print(f"total cars is: {cls.total_car}")

c = Car('bmw')
c1 = Car('odi')
Car.get_total_car()
