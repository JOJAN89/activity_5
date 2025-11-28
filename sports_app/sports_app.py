"""This module defines the SportsApp class.

The SportsApp class provides the main window for the sports
application. It allows interaction with teams, leagues, and players
through a graphical user interface. This class is responsible for
displaying a simple welcome message and demonstrating successful
integration of all activity components.

Example:
    To launch this GUI component, run the main application:

        $ python sports_application.py
"""

__author__ = "jojanpreet kaur"
__version__ = "1.0.0"

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton, QMessageBox
from player.player import Player

class SportsApp(QWidget):
    """Represents the main window of the application
      The SportsApp class displays a table of hard-coded player data,
      along with a button that triggers a welcome message dialog. This
      class is used to demonstrate GUI layout, widget initialization,
      and integration with the Player class.
       """
    

    def __init__(self):
        """Initializes a new instance of the SportsApp class.

        Sets the window title and prepares the application user
        interface.

        Returns:
            None
        """

        super().__init__()
        self.__initialize_widgets()

        self.button.clicked.connect(self.__show_message)

    def __initialize_widgets(self):
        """Initializes the widgets for the application window.

        This method sets the window title, creates the layout,
        populates a QTableWidget with sample Player objects, and
        creates a button used to trigger a welcome dialog.

        Returns:
            None
        """

        self.setWindowTitle("Sports League")

        layout = QVBoxLayout()

        # Create the table
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Position"])

        # Hard-coded data
        players = [
            Player("John Doe", 25, "Forward"),
            Player("Jane Smith", 28, "Midfielder"),
            Player("Jim Brown", 22, "Defender")
        ]

        for i, player in enumerate(players):
            self.table.setItem(i, 0, QTableWidgetItem(player.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(player.age)))
            self.table.setItem(i, 2, QTableWidgetItem(player.position))

        self.table.resizeColumnsToContents()
        
        layout.addWidget(self.table)

        # Create the button
        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.setLayout(layout)

    def __show_message(self):
        """Displays a welcome message to the user.

        This method is executed when the user clicks the button. 

        Returns:
            None
        """
        
        QMessageBox.information(self, "Welcome", "Welcome to the Team!")
