from PyQt5.QtWidgets import (QWidget, QDesktopWidget)
from PyQt5.QtGui import QIcon

class RegisterAccountWindow(QWidget):

    def __init__(self):

        super().__init__()
        
        self.initWindow()
        self.initUI()
        self.show()


    def initWindow(self):
        """Initialize register window"""

        self.setFixedSize(475, 500)
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())

    def initUI(self):
        pass