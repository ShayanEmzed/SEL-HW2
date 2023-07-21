from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def computeArea(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        super().__init__()
        self.__width = width
        self.__height = height

    def computeArea(self):
        return self.__height * self.__width

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width
    
    def get_height(self):
        return self.__height
    
    
    def set_height(self, height):
        self.__height = height


class Square(Shape):

    def __init__(self, side) -> None:
        super().__init__()
        self.__side = side

    def computeArea(self):
        return self.__side * self.__side
    
    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side
