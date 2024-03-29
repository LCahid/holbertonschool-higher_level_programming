#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initialize Square with size attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value: tuple):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the
        current square area.
        """
        return self.__size ** 2

    def my_print(self):
        print(self.__str__())

    def __str__(self) -> str:
        if self.size == 0:
            return ""
        else:
            str = '\n' * self.__position[1]
        for i in range(self.__size):
            str += ' ' * self.position[0]
            str += '#' * self.__size + '\n'
        return str[:-1]
