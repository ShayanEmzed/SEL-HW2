class Rectangle:

    def __init__(self, width, height) -> None:
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
