import math
from plum import dispatch
from PyQt6.QtCore import QPoint, QLine
from wtc import WorldToCanvas
from enum import Enum
from enum import Flag, auto
from typing import Tuple

class mkDir(Flag):
    mkNONE =    auto() # 0b00000000
    mkLEFT =    auto() # 0b00000001 
    mkRIGHT =   auto() # 0b00000010
    mkIN =      auto() # 0b00000100
    mkOUT =     auto() # 0b00001000
    mkSTART =   auto() # 0b00010000 
    mkEND =     auto() # 0b00100000
   
EPS : float = 1e-4
 
 
class MkObj():
    def __init__(self,parent=None):
        super().__init__()
        self.classname = 'MkObj'


from mkpoint import MkPoint
from mkline import MkLine
from mkcircle import MkCircle
from mkarc import MkArc
from mkpoly import MkPoly

# map real points to points in canvas , what 'MkClass'es are doing
# MkPoint vs QPoint
# MkLine vs QPoint
# MkCircle vs QCircle
# MkArc vs QArc
# MkPolygon vs QPolygon
# no inheritance, but has one as property and use its full functionality

