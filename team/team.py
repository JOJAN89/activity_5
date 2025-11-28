"""This module defines the Team class.

The Team class represents a sports team within a league. A team has a
name, a city, and a collection of Player objects. This class provides
functionality for storing basic team information and adding players to
a roster.

Example:
    >>> team = Team("Falcons", "Winnipeg")
    >>> team.add_player(Player("John Doe", 25, "Forward"))
    >>> print(team)
    Team: Falcons, City: Winnipeg, Players: [...]
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"

from player.player import Player


class Team:
    """Represents a sports team within a league.

    A team contains a name, a city, and a roster of Player instances.
    Players may be added using the add_player() method. This class is
    used by the SportsApp GUI and League class for data integration.
    """

    def __init__(self, name: str, city: str) -> None:
        """Initializes a new instance of the Team class.

        Args:
            name (str): The name of the team.
            city (str): The city the team is based in.

        Raises:
            ValueError: Raised when name or city is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")

        if not isinstance(city, str):
            raise ValueError("City must be a string.")

        self.__name = name
        self.__city = city
        self.__players: list[Player] = []

    @property
    def name(self) -> str:
        """Gets the team name.

        Returns:
            str: The name of the team.
        """
        return self.__name

    @property
    def city(self) -> str:
        """Gets the city the team is based in.

        Returns:
            str: The city of the team.
        """
        return self.__city

    @property
    def players(self) -> list:
        """Gets the list of players assigned to the team.

        Returns:
            list: A list of Player objects.
        """
        return self.__players

    def add_player(self, player: Player) -> None:
        """Adds a player to the team's roster.

        Args:
            player (Player): The player to be added to the team.

        Raises:
            ValueError: Raised when the player is not a Player instance.
        """
        if not isinstance(player, Player):
            raise ValueError("player must be an instance of Player.")

        self.__players.append(player)

    def __str__(self) -> str:
        """Returns a string representation of the team.

        Returns:
            str: A formatted string containing team details, including
            its name, city, and list of players.
        """
        player_details = ", ".join(str(player) for player in self.__players)
        return (
            f"Team: {self.__name}, City: {self.__city}, "
            f"Players: [{player_details}]"
        )


