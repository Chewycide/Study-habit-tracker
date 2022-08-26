from PyQt5.QtWidgets import QWidget, QDesktopWidget

class StartWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initWindow()
        self.show()

    
    def initWindow(self):
        """Initialize window"""

        self.setMinimumSize(800, 600)
        self.setWindowTitle("Login")


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def initUI(self):
        """Initialize layouts and widgets"""