import sys

from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QPoint
from mklib import *

class MkPoint(MkObj):
    def __init__(self, x: float, y: float, parent=None):
        super().__init__()
        self.classname = "MkPoint"
        self._p = QPoint()
        self._x = x
        self._y = y
        self.isconv = False

    @dispatch
    def dist(self, p: "MkPoint") -> float:
        x1 = self._x
        x2 = p._x

        y1 = self._y
        y2 = p._y

        d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

        return d

    @dispatch
    def dist(self, l: "MkLine", b:bool=True) -> float:
        flag = l.is_in_proj(self)
        if b == False and flag == False:
            return flag

        A = l.A
        B = l.B
        C = l.C
        x1 = self.x
        y1 = self.y

        d = (A * x1 + B * y1 + C) / math.sqrt(A * A + B * B)

        return d

    @dispatch
    def dist(self, c: "MkCircle") -> float:
        d = 2.0
        return d

    @dispatch
    def dist(self, a: "MkArc") -> float:
        d = 3.0
        return d

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.isconv = False

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.isconv = False

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, p):
        self._p = p

    def conv(self, wtc: WorldToCanvas):
        self._p = wtc.conv(self)
        self.isconv = True

    @property
    def px(self):
        return self.p.x()

    @property
    def py(self):
        return self.p.y()

    def draw(self, qp: QPainter):
        qp.drawPoint(self.p)

    def __repr__(self):
        return f"MkPoint({self.x}, {self.y}, isconv {self.isconv})"


if __name__ == "__main__":

    class MainWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("MkPoint Test App")
            self.resize(1000, 1000)
            self.qp = None
            self.wtc = None

            self.show()

        def paintEvent(self, e):
            self.qp = QPainter()
            self.qp.begin(self)
            self.wtc = WorldToCanvas(self.qp)
            self.qp.end()

            self.qp.begin(self)
            self.draw_points()
            self.qp.end()

        def draw_points(self):
            p1 = MkPoint(10, 10)
            p2 = MkPoint(5, 5)
            p3 = MkPoint(5, 10)
            l1 = MkLine(p1, p2)
            c1 = MkCircle(p1, 5)
            c2 = MkCircle()
            c2.cen = p2
            c2.rad = 5


            print(p1, p2)
            p1.conv(window.wtc)
            p2.conv(window.wtc)

            self.qp.begin(self)

            pen = QPen()
            pen.setWidth(40)
            pen.setColor(Qt.GlobalColor.red)
            self.qp.setPen(pen)
            p1.draw(self.qp)
            pen.setColor(Qt.GlobalColor.blue)
            self.qp.setPen(pen)
            p2.draw(self.qp)

            self.qp.end()

            print(f"p1 = {p1.px,p1.py}")
            print(f"p2 = {p2.px,p2.py}")
            print(f"dist between p1 and p2 = {p1.dist(p2)}")
            print(f"dist between {p3} and {l1} = {p3.dist(l1)}")
            print(f"dist between p1 and c1 = {p1.dist(c1)}")
            print(f"dist between p1 and c2 = {p1.dist(c2)}")

    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = MainWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()
