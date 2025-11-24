"""This module defines the League class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"

from team.team import Team

class League:
    """Represents a league in a sports organization."""

    def __init__(self, name: str):
        """Initializes a new instance of the League class.

        Args: 
            name (str): The name of the league.

        Raises:
            ValueError: Raised when the name is not a string.
        """

        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        self.__name = name
        self.__teams = []

    @property
    def name(self) -> str:
        """Gets the name of the league."""

        return self.__name

    @property
    def teams(self) -> list:
        """Gets the list of teams in the league.

        Returns:
            A list of Team objects.
        """

        return self.__teams

    def add_team(self, team: list) -> None:
        """Adds a team to the league.

        Args:
            team (Team): The team to be added to the league.
        
        Raises:
            ValueError: Raised when the team is not an instance of Team.
        """

        if not isinstance(team, Team):
            raise ValueError("team must be an instance of Team")
        
        self.__teams.append(team)

    def __str__(self) -> str:
        """Returns a string representation of the league.

        Returns
            str: A string containing the league's details.
        """

        team_details = ', '.join(str(team) for team in self.__teams)
        return f"League: {self.__name}, Teams: [{team_details}]"
