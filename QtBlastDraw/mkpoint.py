from mklib import *

class MkPoint(MkObj):

    def __init__(self,x, y, parent=None):
        super().__init__()
        self.classname = 'MkPoint'
        self._p = QPoint()
        self._x = x
        self._y = y
        self.isconv = False

    def dist(self, p:'MkPoint')->float:
        x1 = self._x
        x2 = p.x

        y1 = self._y
        y2 = p.y

        d = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

        return d

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        self._x = x
        self.isconv = False

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        self._y = y
        self.isconv = False

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self,p):
        self._p = p
        self.isconv = True

    def conv(self,wtc: WorldToCanvas):
        self._p = wtc.conv(self)
        self.isconv = True
        return self._p

    def px(self):
        return self._p.x()

    def py(self):
        return self._p.y()

    def __repr__(self):
        return f"MkPoint({self.x}, {self.y}, isconv {self.isconv})"
