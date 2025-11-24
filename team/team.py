"""This module defines the Team class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"

from  player.player import Player

class Team:
    """Represents a team in a sports league."""

    def __init__(self, name: str, city: str):
        """Initializes a new instance of the Team class.

        Args:
            name (str): The name of the team.
            city (str): The city the team is based in.

        Raises: 
            ValueError: Raised when the name is not a string, or city is
                not a string.
        """

        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        
        self.__name = name
        self.__city = city
        self.__players = []

    @property
    def name(self) -> str:
        """Gets the name of the team.

        Returns:
            str: The name of the team instance.
        """

        return self.__name

    @property
    def city(self) -> str:
        """Gets the city of the team.

        Returns:
            str: The city of the team instance.
        """

        return self.__city

    @property
    def players(self) -> list:
        """Gets a list of players on the team.

        Returns:
            list: A list of players on the team instance.
        """

        return self.__players

    def add_player(self, player: Player) -> None:
        """Adds a player to the team.

        Args: 
            player (Player): The player to be added to the team.

        Raises:
            ValueError: Raised when the player is not an instance of
                Player.
        """

        if not isinstance(player, Player):
            raise ValueError("player must be an instance of Player")
        
        self.__players.append(player)

    def __str__(self) -> str:
        """Returns a string representation of the team.

        Returns
            str: A string containing the team's details.
        """

        player_details = ', '.join(str(player) for player in self.__players)
        return f"Team: {self.__name}, City: {self.__city}, Players: [{player_details}]"
