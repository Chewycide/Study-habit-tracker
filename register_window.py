from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QFormLayout, QVBoxLayout,
                            QHBoxLayout, QLineEdit,
                            QLabel, QPushButton,
                            QFrame, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class RegisterAccountWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initWindow()
        self.initUI()
        self.initStyle()
        self.show()


    def initWindow(self):
        """Initialize register window"""

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 250)
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def initUI(self):
        """Initialize layouts and widgets"""
        
        main_vbox = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.setHorizontalSpacing(10)
        checkbox_vbox = QVBoxLayout()
        checkbox_vbox.setAlignment(Qt.AlignTop)
        button_hbox = QHBoxLayout()


        input_frame = QFrame()
        input_frame.setFixedSize(275, 75)


        username_label = QLabel("Username")
        username_entry = QLineEdit()
        token_label = QLabel("Token")
        token_entry = QLineEdit()


        checkbox_frame = QFrame()
        checkbox_frame.setFixedWidth(275)


        tos_checkbox = QCheckBox("I Agree to the Terms of Service.")


        tos_label = QLabel()
        tos_label.setText('<a href="https://github.com/a-know/Pixela/wiki/Terms-of-Service">Terms Of Service -en</a>')
        tos_label.setOpenExternalLinks(True)


        not_minor_checkbox = QCheckBox("I am not a minor.")


        register_button = QPushButton("Create Account")
        cancel_button = QPushButton("Cancel")



        form_layout.insertRow(0, username_label, username_entry)
        form_layout.insertRow(1, token_label, token_entry)
        input_frame.setLayout(form_layout)
        checkbox_vbox.addWidget(tos_checkbox)
        checkbox_vbox.addWidget(tos_label)
        checkbox_vbox.addWidget(not_minor_checkbox)
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