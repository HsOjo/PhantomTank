from sys import argv

from PyQt5.QtWidgets import QApplication

from .controller.main import MainWindow

class Application:
    def __init__(self):
        self.status = 0
        self.qt = QApplication(argv)

        self.main = MainWindow()

    def start(self):
        self.main.show()
        self.status = self.qt.exec_()
