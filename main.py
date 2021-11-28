import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from Circle import Ui_MainWindow
from random import choice


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        color = (choice((range(0, 255))), choice((range(0, 255))), choice((range(0, 255))))
        qp.setBrush(QColor(*color))
        qp.setPen(QColor(*color))
        x, y = choice(range(10, 590)), choice(range(10, 590))
        r = choice(range(10, 280))
        while not (0 < x - r and x + r < 800 and 0 < y - r and y + r < 500):
            x, y = choice(range(10, 590)), choice(range(10, 590))
            r = choice(range(10, 280))
        qp.drawEllipse(x - r, y - r, 2 * r, 2 * r)
        qp.setBrush(QColor(255, 255, 255))
        qp.setPen(QColor(255, 255, 255))
        qp.drawEllipse(x - r + 3, y - r + 3, 2 * r - 6, 2 * r - 6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
