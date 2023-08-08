from logging import raiseExceptions
import sys
import pytest
from typing import List
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import QtGui
from PyQt6.QtGui import QWheelEvent
from mklib import *

def test_pnt():
    pnts = []

    pnt = MkPoint(0,0)
    pnts.append(pnt)
    pnt = MkPoint(1,1)
    pnts.append(pnt)
    
    assert pnts[0].dist(pnts[1]) == (math.sqrt(2))

    pnts[0].x = 1
    assert pnts[0].x == 1
    pnts[0].y = 2
    assert pnts[0].y == 2


def test_line():
    pnts = []
    lines = []

    pnt = MkPoint(0,0)
    pnts.append(pnt)
    pnt = MkPoint(1,1)
    pnts.append(pnt)
    pnt = MkPoint(-2,2)
    pnts.append(pnt)
    pnt = MkPoint(2,-2)
    pnts.append(pnt)
    pnt = MkPoint(2,0)
    pnts.append(pnt)
    pnt = MkPoint(2,2)
    pnts.append(pnt)

    line = MkLine(pnts[0],pnts[1])
    lines.append(line)
    line = MkLine(pnts[2],pnts[3])
    lines.append(line)
    line = MkLine(pnts[0], pnts[2])
    lines.append(line)
    line = MkLine(pnts[1], pnts[3])
    lines.append(line)
    line = MkLine(pnts[4],pnts[5])
    lines.append(line)
    
    assert lines[0].get_p(0).x == pnts[0].x and lines[0].get_p(0).y == pnts[0].y
    assert lines[0].get_p(1).x == pnts[1].x and lines[0].get_p(1).y == pnts[1].y
    assert lines[0].get_t(pnts[0]) == 0 and lines[0].get_t(pnts[1]) == 1
    assert lines[0].get_t(pnts[2]) == False
    assert lines[0].is_inter(lines[1]) == True
    assert lines[2].is_inter(lines[3]) == False
    assert lines[0].get_proj(lines[4]).x == 2 and lines[0].get_proj(lines[4]).y == 2 
    assert abs(lines[1].dist(pnts[1]) - math.sqrt(2)) < EPS
    assert lines[0].trim(lines[1],mkDir.mkLEFT).p1.x == 0 and lines[0].trim(lines[1],mkDir.mkLEFT).p1.y == 0
    assert lines[0].trim(lines[1],mkDir.mkLEFT).p2.x == 2 and lines[0].trim(lines[1],mkDir.mkLEFT).p2.y == -2
    assert lines[0].extend(lines[4]).p2.x == 2 and lines[0].extend(lines[4]).p2.y == 2
    lines[0].p2 = MkPoint(1,1)
    assert lines[0].p2.x == 1 and lines[0].p2.y == 1
    print(pnts[0], pnts[1],pnts[0].dist(pnts[1]),lines[0].Len)
    assert lines[0].Len == math.sqrt(2)  # after extend the line 
    assert lines[0].get_inter(lines[1]).x == 0 and lines[0].get_inter(lines[1]).y == 0
    assert lines[0].is_in_proj(pnts[5]) is False
    assert lines[0].is_in_proj(pnts[2]) is True
    assert lines[0].get_in_proj(pnts[2]).x == 0 and lines[0].get_in_proj(pnts[2]).y == 0
    assert abs(lines[0].offset(1,mkDir.mkRIGHT).p1.x - 1 / math.sqrt(2)) < EPS
    assert abs(lines[0].offset(1,mkDir.mkRIGHT).p1.y + 1 / math.sqrt(2)) < EPS


def test_cir():
    cirs = []
    cir = MkCircle()
    cir.cen = MkPoint(0,0)
    cir.rad = 1
    cirs.append(cir)

    arcs = []
    arc = MkArc()
    arc.cen = MkPoint(1,1)
    arc.rad = 1
    arc.sang = 0
    arc.eang = 180

    with pytest.raises(Exception):
      cir.dist(arc) 
  
    assert abs(cir.get_pnt(90).x) < EPS and abs(cir.get_pnt(90).y - 1) < EPS  
    assert abs(cir.whang(MkPoint(0,1)) - 90) < EPS
        



        


def test_arc():
  pass

