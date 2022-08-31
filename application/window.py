import requests
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QGridLayout, QHBoxLayout,
                            QLineEdit, QLabel,
                            QPushButton, QFrame,
                            QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from application.register_window import RegisterAccountWindow
from application.user_window import UserWindow


GRAPHID = "study1"
LOGO_WIDTH = 150
LOGO_HEIGHT = LOGO_WIDTH

class StartWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.username = ""

        self.initWindow()
        self.initUI()
        self.initStyle()
        self.show()

    
    def initWindow(self):
        """Initialize window"""

        self.setFixedSize(475, 350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def initUI(self):
        """Initialize layouts and widgets"""

        self.error_msg = QMessageBox()
        self.error_msg.setIcon(QMessageBox.Critical)
        self.error_msg.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))
        self.error_msg.setWindowTitle("ERROR")


        main_vbox = QVBoxLayout()
        main_hbox = QHBoxLayout()


        grid = QGridLayout()
        grid.setContentsMargins(50, 10, 50, 10)
        grid.setSpacing(1)
        logo_hbox = QHBoxLayout()
        

        frame = QFrame()
        frame.setFixedSize(400, 300)


        self.pixela_logo = QLabel("")
        self.pixela_logo.setMaximumSize(LOGO_WIDTH, LOGO_HEIGHT)
        self.pixela_logo.setPixmap(QPixmap("assets/PIXELA_ORIGINAL_e.png").scaled(LOGO_WIDTH,LOGO_HEIGHT,Qt.KeepAspectRatio))


        self.usern_label = QLabel("Username:")
        self.usern_label.setMaximumSize(75, 20)


        self.usern_entry = QLineEdit()
        self.usern_entry.setMaximumSize(150, 20)


        button_hbox = QHBoxLayout()
        self.login_button = QPushButton("Login")
        self.login_button.setFixedSize(60, 40)
        self.login_button.clicked.connect(self.login)


        self.register_button = QPushButton("Register")
        self.register_button.setFixedSize(60, 40)
        self.setToolTip("Dont have a Pixela account?")
        self.register_button.clicked.connect(self.register)


        main_vbox.addLayout(main_hbox)
        main_hbox.addWidget(frame)

        frame.setLayout(grid)
        grid.addLayout(logo_hbox, 0, 0, 1, 2)
        logo_hbox.addWidget(self.pixela_logo)

        grid.addWidget(self.usern_label, 1, 0)
        grid.addWidget(self.usern_entry, 1, 1)

        grid.addLayout(button_hbox, 2, 0, 1, 2)
        button_hbox.addWidget(self.login_button)
        button_hbox.addWidget(self.register_button)

        self.setLayout(main_vbox)


    def initStyle(self):
        """Use stylesheet file"""

        with open("styles/start_window.qss", "r") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())


    def register(self):
        """register to pixela"""

        self.register_window = RegisterAccountWindow()


    def login(self):
        """login to pixela"""

        self.username = self.usern_entry.text()
        self.user_window = UserWindow()
        # try:
        #     login_response = requests.get(f"https://pixe.la/v1/users/{self.username}/graphs/{GRAPHID}")
        #     login_response.raise_for_status()
        # except requests.exceptions.HTTPError:
        #     self.error_msg.setText(f"User '{self.username}' does not exist.")
        #     self.error_msg.exec()
        # else:
        #     print(login_response.text)

        # NOTE: Code is commented above since user_window.py is still being tested.