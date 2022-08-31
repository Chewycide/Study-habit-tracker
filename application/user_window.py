import requests
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QPushButton, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class UserWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initWindow()
        self.initUI()
        self.initStyle()
        self.show()

    
    def initWindow(self):
        """Initialize user window after login"""

        self.setMinimumSize(500, 500)
        self.showMaximized()
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


    def initUI(self):
        pass


    def initStyle(self):
        pass