from io import BytesIO

from PIL.Image import open as img_open
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from ..common import *
from ..view.main import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.sa_result.setPalette(QPalette(QColor(255, 255, 255)))

        self.img_inner = None  # type: Image
        self.img_outer = None  # type: Image
        self.img_result = None  # type: Image

        self.pb_inner.clicked.connect(self.__pb_inner_clicked)
        self.pb_outer.clicked.connect(self.__pb_outer_clicked)
        self.pb_build.clicked.connect(self.__pb_build_clicked)
        self.pb_save.clicked.connect(self.__pb_save_clicked)
        self.cb_dark.clicked.connect(self.__cb_dark_clicked)

    def __pb_inner_clicked(self):
        [path, _] = QFileDialog.getOpenFileName(parent=self, caption='Set Inner Image')

        if path != '':
            with open(path, 'br') as io:
                self.img_inner = img_open(io).copy()
                io.seek(0)

                pixmap = QPixmap()
                pixmap.loadFromData(io.read())
                self.l_inner.setPixmap(pixmap)

    def __pb_outer_clicked(self):
        [path, _] = QFileDialog.getOpenFileName(parent=self, caption='Set Outer Image')

        if path != '':
            with open(path, 'br') as io:
                self.img_outer = img_open(io).copy()
                io.seek(0)

                pixmap = QPixmap()
                pixmap.loadFromData(io.read())
                self.l_outer.setPixmap(pixmap)

    def __pb_build_clicked(self):
        self.img_result = build_phantom_tank(self.img_inner, self.img_outer)

        with BytesIO() as io:
            self.img_result.save(io, 'png')
            io.seek(0)

            data = io.read()

        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.l_result.setPixmap(pixmap)

    def __cb_dark_clicked(self):
        if self.cb_dark.isChecked():
            self.sa_result.setPalette(QPalette(QColor(0, 0, 0)))
        else:
            self.sa_result.setPalette(QPalette(QColor(255, 255, 255)))

    def __pb_save_clicked(self):
        if self.img_result is not None:
            [path, _] = QFileDialog.getSaveFileName(parent=self, caption='Save Result Image', filter='PNG Files (*.png)')

            if path != '':
                with open(path, 'bw') as io:
                    self.img_result.save(io, 'png')
