import requests
import datetime as dt
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                            QPushButton, QLabel,
                            QVBoxLayout, QHBoxLayout,
                            QFrame, QGridLayout,
                            )
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class UserWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.last_date = "yyyyMMdd"
        self.last_hrs = "0"
        self.today_date = "yyyyMMdd"
        self.today_hrs = "0"
        self.getDate()


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
        """Initialize widgets"""

        main_vbox = QVBoxLayout()
        main_vbox.setAlignment(Qt.AlignTop)


        top_frame = QFrame()
        top_frame.setMaximumHeight(100)
        top_frame.setContentsMargins(20, 20, 20, 20)
        top_frame_grid = QGridLayout()
        top_frame_grid.setHorizontalSpacing(100)
        top_frame_grid.setContentsMargins(10, 10, 10, 10)
        top_frame_grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        top_frame.setLayout(top_frame_grid)


        recent_date_label = QLabel("Last study date:")
        recent_date_label_data = QLabel(f"{self.last_date}")
        recent_hrs_label = QLabel("Recent study hours:")
        recent_hrs_label_data = QLabel(f"{self.last_hrs} hr/s")


        bottom_frame = QFrame()
        bottom_frame.setMaximumHeight(600)
        bottom_frame.setContentsMargins(20, 20, 20, 20)
        bottom_frame_grid = QGridLayout()
        bottom_frame_grid.setHorizontalSpacing(30)
        bottom_frame_grid.setContentsMargins(10, 10, 10, 10)
        bottom_frame_grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        bottom_frame.setLayout(bottom_frame_grid)


        today_date_label = QLabel("Date today:")
        today_date_label_data = QLabel(f"{self.today_date}")
        today_hrs_label = QLabel(f"Hrs studied today: {self.today_hrs} hr/s")
        today_hrs_input = QLineEdit()


        post_pixel_button = QPushButton("POST")
        post_pixel_button.setFixedSize(60, 40)


        main_vbox.addWidget(top_frame)

        main_vbox.addWidget(bottom_frame)
        bottom_frame_grid.addWidget(recent_date_label, 0, 0)
        bottom_frame_grid.addWidget(recent_date_label_data, 0, 1)
        bottom_frame_grid.addWidget(recent_hrs_label, 1, 0)
        bottom_frame_grid.addWidget(recent_hrs_label_data, 1, 1)
        bottom_frame_grid.addWidget(today_date_label, 2, 0)
        bottom_frame_grid.addWidget(today_date_label_data, 2, 1)
        bottom_frame_grid.addWidget(today_hrs_label, 3, 0)
        bottom_frame_grid.addWidget(today_hrs_input, 3, 1)
        bottom_frame_grid.addWidget(post_pixel_button, 2, 2, 2, 1)

        self.setLayout(main_vbox)


    def initStyle(self):
        """Initialize stylesheet"""

        with open("styles/user_window.qss", "r") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())


    def getDate(self):
        """Get the date yesterday and today"""

        yesterday = dt.datetime.now() - dt.timedelta(1)
        yd_user = yesterday.strftime("%B %d, %Y")
        yd_pixela = yesterday.strftime("%Y%m%d")

        today = dt.datetime.now()
        td_user = today.strftime("%B %d, %Y")
        td_pixela = today.strftime("%Y%m%d")


        self.last_date = yd_user
        self.today_date = td_user