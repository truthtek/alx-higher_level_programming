#!/usr/bin/python3
""" Working on oop with python """

class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """ Initialize the class

        Args:
           size (int, optional): size of the square (default is 0)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
