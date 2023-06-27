
https://intranet.alxswe.com/projects/245#:~:text=1%2Dmain.py-,%23!/usr/bin/python3%0Asafe_print_integer%20%3D%20__import__(%271%2Dsafe_print_integer%27).safe_print_integer%0A%0Avalue%20%3D%2089%0Ahas_been_print,value)%0Aif%20not%20has_been_print%3A%0A%20%20%20%20print(%22%7B%7D%20is%20not%20an%20integer%22.format(value)),-guillaume%40ubuntu%3A~/0x05
n-classes
0x06-python-classes



README.md


Python - Classes and Objects

In this project, I began practicing object-oriented programming using classes and objects in Python. I learned about attributes, methods, and properties as well as data abstraction, data encapsulation, and information hiding.

=============================

0-square.py


#!/usr/bin/python3

"""Define a class Square."""



class Square:

        """Represent a square."""

            pass


        =============================

        1-square.py


        #!/usr/bin/python3

        """Define a class Square."""



        class Square:

                """Represent a square."""


                    def __init__(self, size):

                                """Initialize a new Square.


                                        Args:

                                                    size (int): The size of the new square.

                                                            """

                                                                    self.__size = size


                                                                    =============================

                                                                    2-square.py


                                                                    #!/usr/bin/python3

                                                                    """Define a class Square."""



                                                                    class Square:

                                                                            """Represent a square."""


                                                                                def __init__(self, size=0):

                                                                                            """Initialize a new Square.


                                                                                                    Args:

                                                                                                                size (int): The size of the new square.

                                                                                                                        """

                                                                                                                                if not isinstance(size, int):

                                                                                                                                                raise TypeError("size must be an integer")

                                                                                                                                                    elif size < 0:

                                                                                                                                                                    raise ValueError("size must be >= 0")

                                                                                                                                                                        self.__size = size


                                                                                                                                                                        =============================

                                                                                                                                                                        3-square.py


                                                                                                                                                                        #!/usr/bin/python3

                                                                                                                                                                        """Define a class Square."""



                                                                                                                                                                        class Square:

                                                                                                                                                                                """Represent a square."""


                                                                                                                                                                                    def __init__(self, size=0):

                                                                                                                                                                                                """Initialize a new square.


                                                                                                                                                                                                        Args:

                                                                                                                                                                                                                        size (int): The size of the new square.

                                                                                                                                                                                                                                """

                                                                                                                                                                                                                                        if not isinstance(size, int):

                                                                                                                                                                                                                                                        raise TypeError("size must be an integer")

                                                                                                                                                                                                                                                            elif size < 0:

                                                                                                                                                                                                                                                                            raise ValueError("size must be >= 0")

                                                                                                                                                                                                                                                                                self.__size = size


                                                                                                                                                                                                                                                                                    def area(self):

                                                                                                                                                                                                                                                                                                """Return the current area of the square."""

                                                                                                                                                                                                                                                                                                        return (self.__size * self.__size)


                                                                                                                                                                                                                                                                                                    =============================

                                                                                                                                                                                                                                                                                                    4-square.py


                                                                                                                                                                                                                                                                                                    #!/usr/bin/python3

                                                                                                                                                                                                                                                                                                    """Define a class Square."""



                                                                                                                                                                                                                                                                                                    class Square:

                                                                                                                                                                                                                                                                                                            """Represent a square."""


                                                                                                                                                                                                                                                                                                                def __init__(self, size=0):

                                                                                                                                                                                                                                                                                                                            """Initialize a new square.


                                                                                                                                                                                                                                                                                                                                    Args:

                                                                                                                                                                                                                                                                                                                                                size (int): The size of the new square.

                                                                                                                                                                                                                                                                                                                                                        """

                                                                                                                                                                                                                                                                                                                                                                self.size = size


                                                                                                                                                                                                                                                                                                                                                                    @property

                                                                                                                                                                                                                                                                                                                                                                        def size(self):

                                                                                                                                                                                                                                                                                                                                                                                    """Get/set the current size of the square."""

                                                                                                                                                                                                                                                                                                                                                                                            return (self.__size)

                                                                                                                                                                                                                                                                                                                                                                                            @size.setter

                                                                                                                                                                                                                                                                                                                                                                                                def size(self, value):

                                                                                                                                                                                                                                                                                                                                                                                                            if not isinstance(value, int):

                                                                                                                                                                                                                                                                                                                                                                                                                            raise TypeError("size must be an integer")

                                                                                                                                                                                                                                                                                                                                                                                                                                elif value < 0:

                                                                                                                                                                                                                                                                                                                                                                                                                                                raise ValueError("size must be >= 0")

                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.__size = value


                                                                                                                                                                                                                                                                                                                                                                                                                                                        def area(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """Return the current area of the square."""

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return (self.__size * self.__size)
