import math

class Cylinder:
    def __init__(self, radius=1.0, length=1.0):
        self.__radius = radius
        self.__length = length

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    def area(self):
        return 2 * math.pi * self.__radius * (self.__radius + self.__length)

    def volume(self):
        return self.area() * self.__length

    def CylinderInfo(self):
        print(f"Radius: {self.radius}")
        print(f"Length: {self.length}")
        print(f"Area: {self.area():.2f}")
        print(f"Volume: {self.volume():.2f}")