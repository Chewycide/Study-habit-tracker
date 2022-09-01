import requests
import json
from pathlib import Path
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QFormLayout, QVBoxLayout,
                            QHBoxLayout, QLineEdit,
                            QLabel, QPushButton,
                            QFrame, QCheckBox,
                            QComboBox, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


GRAPHID = "study1"
GRAPHNAME = "Study Habit Tracker"
GRAPHUNIT = "hr/s"
GRAPHTYPE = "float"


class RegisterAccountWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.username = ""
        self.token = ""
        self.password = ""
        self.agreeTOS = "no"
        self.notMinor = "no"


        self.initWindow()
        self.initUI()
        self.initStyle()
        self.show()


    def initWindow(self):
        """Initialize register window"""

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 300)
        self.setWindowTitle("Register")
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
        form_layout = QFormLayout()
        form_layout.setHorizontalSpacing(10)
        checkbox_vbox = QVBoxLayout()
        checkbox_vbox.setAlignment(Qt.AlignTop)
        color_form_layout = QFormLayout()
        button_hbox = QHBoxLayout()


        input_frame = QFrame()
        input_frame.setFixedSize(275, 75)


        username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("[a-z][a-z0-9-]{1,32}")


        token_label = QLabel("Token:")
        self.token_entry = QLineEdit()
        self.token_entry.setPlaceholderText("[ -~]{8,128}")


        checkbox_frame = QFrame()
        checkbox_frame.setFixedWidth(275)


        self.tos_checkbox = QCheckBox("I Agree to the Terms of Service.")
        

        tos_label = QLabel()
        tos_label.setText('<a href="https://github.com/a-know/Pixela/wiki/Terms-of-Service">Terms Of Service -en</a>')
        tos_label.setOpenExternalLinks(True)


        self.not_minor_checkbox = QCheckBox("I am not a minor/I have parental consent.")

        color_box_label = QLabel("Graph color:")
        self.color_box = QComboBox()
        colors = ["green", "red", "blue", "yellow", "purple", "black"]
        for color in colors:
            self.color_box.addItem(color)


        register_button = QPushButton("Create Account")
        register_button.clicked.connect(self.register)


        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)


        form_layout.insertRow(0, username_label, self.username_entry)
        form_layout.insertRow(1, token_label, self.token_entry)
        input_frame.setLayout(form_layout)
        checkbox_vbox.addWidget(self.tos_checkbox)
        checkbox_vbox.addWidget(tos_label)
        checkbox_vbox.addWidget(self.not_minor_checkbox)
        color_form_layout.insertRow(0, color_box_label, self.color_box)
        checkbox_vbox.addLayout(color_form_layout)
        checkbox_vbox.addStretch(1)
        button_hbox.addWidget(register_button)
        button_hbox.addWidget(cancel_button)
        checkbox_vbox.addLayout(button_hbox)
        checkbox_frame.setLayout(checkbox_vbox)
        main_vbox.addWidget(input_frame)
        main_vbox.addWidget(checkbox_frame)
        self.setLayout(main_vbox)


    def initStyle(self):
        """Initialize stylesheet file"""

        with open("styles/register_window.qss", "r") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())


    def graph_color(self):
        """get QComboBox english lang color then return japanese lang equivalent"""

        chosen_color = self.color_box.currentText()
        if chosen_color == "green":
            return "shibafu"
        elif chosen_color == "red":
            return "momiji"
        elif chosen_color == "blue":
            return "sora"
        elif chosen_color == "yellow":
            return "ichou"
        elif chosen_color == "purple":
            return "ajisai"
        elif chosen_color == "black":
            return "kuro"


    def register(self):
        """register with given info"""

        self.username = self.username_entry.text()
        self.token = self.token_entry.text()
        if  self.tos_checkbox.isChecked():
            self.agreeTOS = "yes"
        if self.not_minor_checkbox.isChecked():
            self.notMinor = "yes"
        self.color = self.graph_color()
        

        register_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": self.agreeTOS,
            "notMinor": self.notMinor
        }

        graph_params = {
            "id": GRAPHID,
            "name": GRAPHNAME,
            "unit": GRAPHUNIT,
            "type": GRAPHTYPE,
            "color": self.color
        }

        header = {"X-USER-TOKEN": self.token}

########## save successfully created user to local file ######### 

        registered_account_info = {
            "USERNAME": self.username,
            "TOKEN": self.token,
            "AGREE_TOS": self.agreeTOS,
            "NOT_MINOR": self.notMinor,
            "PIXELA_GRAPH": f"https://pixe.la/v1/users/{self.username}/graphs/{GRAPHID}.html",
            "ACCOUNT_WEBSITE": f"https://pixe.la/@{self.username}"
        }

        register_params_json = {self.username : registered_account_info}
        try:
            with open(f"user/users.json", "r") as user_file:
                user_data = json.load(user_file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_dir = Path("user/").mkdir(parents=True, exist_ok=True)
            user_data = register_params_json
            self.connectAPI(register_params, graph_params, header)
        else:
            # if user exists locally dont create, else create user
            if self.username in user_data:
                self.error_msg.setText("User exists locally.\nCreate another username.")
                self.error_msg.exec()
            else: # TODO: IF EXISTING ONLINE DONT CREATE
                user_data.update(register_params_json)
                self.connectAPI(register_params, graph_params, header)
        finally: # save
            with open(f"user/users.json", "w") as user_file:
                json.dump(user_data, user_file, indent=4)


    def connectAPI(self, register_params, graph_params, header):
        """connect to Pixela api"""

        user_create_response = requests.post("https://pixe.la/v1/users", json=register_params)
        print(user_create_response.status_code, user_create_response.text)
        user_create_response.raise_for_status()

        graph_create_response = requests.post(f"https://pixe.la/v1/users/{self.username}/graphs", json=graph_params, headers=header)
        print(graph_create_response.status_code, graph_create_response.text)
        graph_create_response.raise_for_status()

        print(f"https://pixe.la/v1/users/{self.username}/graphs/{GRAPHID}.html")
        