#!/usr/bin/python3
"""Defining a class square, inheriting from the class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the new square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class
        Args:
        size: the size of the new square(width and height)
        width: the width of the square
        height: the height of the square
        x: the x coordinate of the square
        y: the y coordinate of the square
        id: represents the identity of the square

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting the size of the square"""
        return self.height

    @size.setter
    def size(self, value):
        """Setting the value of the size
        - The setter should assign (in this order) the width and the height
        - with the same value
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Override string representation of the class
        in the format:
        [Square] (<id>) <x>/<y> - <size>
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )

    def update(self, *args, **kwargs):
        """
        Method that assigns arguments to each attribute
        Args:
        args: number of arguments
        - first argument represents the id attribute
        - second argument represents the size attribute
        - third argument represents the x attribute
        - fourth argument represents the y attribute

        kwargs: represents args with a key = value format

        """

        if args or len(args) != 0:
            g = 0
            for arg in args:
                if g == 0:
                    if arg is None:
                        self.__init__(self.id, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif g == 1:
                    self.size = arg
                elif g == 2:
                    self.x = arg
                elif g == 3:
                    self.y = arg
                g += 1

        elif kwargs and len(kwargs) != 0:
            """ assigning a key/value argument to attributes
            -   Argument order is not important.
            """

            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the class"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
