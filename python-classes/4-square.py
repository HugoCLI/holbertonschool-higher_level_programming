#!/usr/bin/python3
"""Square"""


class Square:
    """Init Square"""
    def __init__(self, size=0):
       self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be an integer")
        self.__size = value
