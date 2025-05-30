#!/usr/bin/python3

"""classe square heritant de rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Represente un rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
