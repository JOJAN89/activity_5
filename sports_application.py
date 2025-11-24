"""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
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
