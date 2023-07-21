class Rectangle:

    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

    def computeArea(self):
        return self.__height * self.__width
