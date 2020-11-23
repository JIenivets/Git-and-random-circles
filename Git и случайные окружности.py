import sys

from random import randint

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush, QPainterPath


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        self.qp = QPainter()
        self.path = QPainterPath()
        # Начинаем процесс рисования
        self.qp.begin(self)
        self.draw_flag()
        # Завершаем рисование
        self.qp.end()

    def draw_flag(self):
        a = randint(5, 450)
        self.qp.setBrush(QColor('yellow'))
        # Рисуем прямоугольник заданной кистью
        self.qp.drawEllipse(250 - a / 2, 275 - a / 2, a, a)




class MyWidget2(MyWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1000, 500, 500, 600)

        self.btn = QtWidgets.QPushButton('*тут должна быть надпись*', self)
        self.btn.setGeometry(QtCore.QRect(125, 0, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn.setFont(font)

        self.btn.clicked.connect(self.da)

    def da(self):
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget2()
    ex.show()
    sys.exit(app.exec_())