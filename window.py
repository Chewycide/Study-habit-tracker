from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QGridLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

LOGO_WIDTH = 150
LOGO_HEIGHT = LOGO_WIDTH

class StartWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initWindow()
        self.initUI()
        self.show()

    
    def initWindow(self):
        """Initialize window"""

        self.setFixedSize(475, 350)
        self.setWindowTitle("Login")


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def initUI(self):
        """Initialize layouts and widgets"""

        grid = QGridLayout()
        grid.setContentsMargins(50, 10, 50, 10)
        grid.setSpacing(1)
        logo_hbox = QHBoxLayout()
        button_hbox = QHBoxLayout()
        

        self.pixela_logo = QLabel("", self)
        self.pixela_logo.setMaximumSize(LOGO_WIDTH, LOGO_HEIGHT)
        self.pixela_logo.setPixmap(QPixmap("assets/PIXELA_ORIGINAL.png").scaled(LOGO_WIDTH,LOGO_HEIGHT,Qt.KeepAspectRatio))


        self.usern_label = QLabel("Username", self)
        self.usern_label.setMaximumSize(75, 20)


        self.usern_entry = QLineEdit()
        self.usern_entry.setMaximumSize(150, 20)


        self.login_button = QPushButton("Login")
        self.login_button.setFixedSize(60, 40)


        grid.addLayout(logo_hbox, 0, 0, 1, 2)
        logo_hbox.addWidget(self.pixela_logo)
        grid.addWidget(self.usern_label, 1, 0)
        grid.addWidget(self.usern_entry, 1, 1)
        grid.addLayout(button_hbox, 2, 0, 1, 2)
        button_hbox.addWidget(self.login_button)
        self.setLayout(grid)
