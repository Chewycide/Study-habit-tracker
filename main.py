import sys
from window import StartWindow
from PyQt5.QtWidgets import QApplication


def main():

    app = QApplication(sys.argv)

    window = StartWindow()

    sys.exit(app.exec())