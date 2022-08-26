import sys
from window import Window
from PyQt5.QtWidgets import QApplication


def main():

    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec())