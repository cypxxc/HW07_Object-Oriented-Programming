class Rectangle:
    def __init__(self, width=1.0, height=1.0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def RectangleInfo(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area():.2f}")