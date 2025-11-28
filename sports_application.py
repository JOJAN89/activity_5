"""A client program used to launch and verify the correctness of the
sports application classes.

This module serves as the entry point for the Sports Application. It
creates the application instance and launches the graphical user
interface provided by the SportsApp class.

Example:
    To run the sports application:

        $ python sports_application.py
"""

__author__ = "jojanpreet kaur"
__version__ = "1.0.0"

from sports_app.sports_app import SportsApp

# GIVEN:
from PySide6.QtWidgets import QApplication
import sys

# GIVEN:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SportsApp()
    window.show()
    sys.exit(app.exec())
