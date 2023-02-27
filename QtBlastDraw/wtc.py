from PyQt5.QtCore import QPoint
# from mklib import *


class WorldToCanvas():
    def __init__(self,canvas,parent=None):
        super().__init__()
        
        self._canvas = canvas
        __x = self._canvas.viewport().width()/2.0
        __y = self._canvas.viewport().height()/2.0
        
        self._cen = QPoint(int(__x), int(__y))
        self._scale = 20

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self,_canvas):
        self._canvas = _canvas

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self,_scale):
        self._scale = _scale

    def conv(self, pnt):
        ix = int(pnt.x * self.scale + self._cen.x())
        iy = int(-pnt.y * self.scale + self._cen.y())
        p = QPoint(ix, iy)
        return p
    
    def __repr__(self):
        return f'World to Canvas center {self._cen} and scale {self._scale}'
