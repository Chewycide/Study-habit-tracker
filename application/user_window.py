import requests
import datetime as dt
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                            QPushButton, QLabel,
                            QVBoxLayout, QHBoxLayout,
                            QFrame, QGridLayout,
                            )
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer

GRAPHID = "study1"

class UserWindow(QWidget):

    def __init__(self, user, token):

        super().__init__()

        self.username = user
        self.token = token
        self.last_date = "yyyyMMdd"
        self.last_hrs = "0"
        self.today_date = "yyyyMMdd"
        self.today_hrs = "0"
        self.getDate()
        self.getSVG()

        self.initWindow()
        self.initUI()
        self.initStyle()
        self.show()

    
    def initWindow(self):
        """Initialize user window after login"""

        self.setMinimumWidth(800)
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


    def initUI(self):
        """Initialize widgets"""

        main_vbox = QVBoxLayout()
        main_vbox.setAlignment(Qt.AlignTop)


        top_frame = QFrame()
        top_frame_hbox = QHBoxLayout()
        
        top_frame_hbox.setContentsMargins(10, 10, 10, 10)
        top_frame_hbox.setAlignment(Qt.AlignTop)
        top_frame.setLayout(top_frame_hbox)


        bottom_frame = QFrame()
        bottom_frame.setMaximumHeight(1000)
        bottom_frame.setContentsMargins(20, 20, 20, 20)
        bottom_frame_grid = QGridLayout()
        bottom_frame_grid.setHorizontalSpacing(30)
        bottom_frame_grid.setContentsMargins(10, 10, 10, 10)
        bottom_frame_grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        bottom_frame.setLayout(bottom_frame_grid)


        recent_date_label = QLabel("Date Yesterday:")
        recent_date_label_data = QLabel(f"{self.last_date}")
        recent_hrs_label = QLabel("Yesterday study hours:")
        recent_hrs_label_data = QLabel(f"{self.last_hrs} hr/s")


        today_date_label = QLabel("Date today:")
        today_date_label_data = QLabel(f"{self.today_date}")
        today_hrs_label = QLabel(f"Hrs studied today: {self.today_hrs} hr/s")
        today_hrs_input = QLineEdit()


        post_pixel_button = QPushButton("POST")
        post_pixel_button.setFixedSize(60, 40)


        main_vbox.addWidget(top_frame)
        top_frame_hbox.addWidget(self.svg_widget, alignment=Qt.AlignCenter)

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

        self.getPixel(yd_pixela)


    def getPixel(self, yestrd):
        """Get pixel info from yesterday"""


        header_token = {"X-USER-TOKEN": self.token}
        get_pixel_response = requests.get(f"https://pixe.la/v1/users/{self.username}/graphs/{GRAPHID}/{yestrd}", headers=header_token)
        print(get_pixel_response.text)


    def getSVG(self):
        """Get the graph SVG using Pixela's API as an image then embed to the window"""

        svg_response = requests.get(f"https://pixe.la/v1/users/{self.username}/graphs/{GRAPHID}")
        graph_svg = svg_response.text
        svg_bytes = bytearray(graph_svg, encoding='utf-8')
        self.svg_widget = QImage.fromData(svg_bytes)
        self.get_size = QSvgRenderer(svg_bytes)
        self.svg_widget = QSvgWidget()
        self.svg_widget.load(svg_bytes)

        self.svg_widget.setFixedSize(self.get_size.defaultSize())