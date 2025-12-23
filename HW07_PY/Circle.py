from math import radians
import math

class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value
    
    def area(self):
        return math.pi * self.__radius * (self.__radius **2)

    def CircleInfo(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area():.2f}")
    