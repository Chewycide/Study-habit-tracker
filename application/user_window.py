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

        top_frame = QFrame()
        top_frame.setMaximumSize(500, 500)
        top_frame.setContentsMargins(20, 20, 20, 20)
        top_frame_grid = QGridLayout()
        top_frame_grid.setContentsMargins(10, 10, 10, 10)
        top_frame_grid.setAlignment(Qt.AlignTop)
        top_frame.setLayout(top_frame_grid)


        recent_date_label = QLabel(f"Last study date: {self.last_date}")
        recent_hrs_label = QLabel(f"Recent study hours: {self.last_hrs} hr/s")


        bottom_frame = QFrame()
        bottom_frame.setContentsMargins(20, 20, 20, 20)
        bottom_frame_grid = QGridLayout()
        bottom_frame_grid.setHorizontalSpacing(50)
        bottom_frame_grid.setContentsMargins(10, 10, 10, 10)
        bottom_frame_grid.setAlignment(Qt.AlignTop)
        bottom_frame.setLayout(bottom_frame_grid)


        today_date_label = QLabel(f"Date today: {self.today_date}")
        today_hrs_label = QLabel(f"Hrs studied today: {self.today_hrs} hr/s")

        today_hrs_input = QLineEdit()


        main_vbox.addWidget(top_frame)
        top_frame_grid.addWidget(recent_date_label, 0, 0)
        top_frame_grid.addWidget(recent_hrs_label, 1, 0)

        main_vbox.addWidget(bottom_frame)
        bottom_frame_grid.addWidget(today_date_label, 0, 0)
        bottom_frame_grid.addWidget(today_hrs_label, 1, 0)
        bottom_frame_grid.addWidget(today_hrs_input, 1, 1)
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