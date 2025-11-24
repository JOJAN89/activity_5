"""This module defines the League class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class Player:
    """Represents a player on a sports team."""

    def __init__(self, name: str, age: int, position: str):
        """Initializes a new instance of the Player class.

        Args:
            name (str): The name of the player.
            age (int): The age of the player.
            position (str): The position of the player on the team.

        Raises
            ValueError: Raised when the name is not a string, age is not
                an integer, or position is not a string.
        """

        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        
        if not isinstance(position, str):
            raise ValueError("Position must be a string")
        
        self.__name = name
        self.__age = age
        self.__position = position

    @property
    def name(self) -> str:
        """Gets the name of the player.

        Returns:
            str: The name of the player instance.
        """

        return self.__name

    @property
    def age(self) -> int:
        """Gets the age of the player.

        Returns:
            int: The age of the player instance.
        """

        return self.__age

    @property
    def position(self) -> str:
        """Gets the position of the player.

        Returns:
            str: The position of the player instance.
        """

        return self.__position

    def __str__(self) -> str:
        """Returns a string representation of the player.

        Returns
            str: A string containing the player's details.
        """

        return f"Name: {self.__name}, Age: {self.__age}, Position: {self.__position}"
