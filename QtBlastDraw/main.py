import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import QtGui
from PyQt6.QtGui import QWheelEvent
from mklib import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.qp = None # QPainter()
        self.wtc = None # WorldToCanvas(self.qp)
        self.bcen = None

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('drawing test')

        # changing the background color to yellow
        self.setStyleSheet("background-color: gray;")        

        self.show()
        self.mx = 0
        self.my = 0

    def paintEvent(self, e):
        if self.qp == None:    
            self.qp = QPainter()
            self.qp.begin(self)
            self.wtc = WorldToCanvas(self.qp)
            self.qp.end()

        self.qp.begin(self)
        # self.draw_arc(self.qp)
        # self.draw_sc(self.qp)
        # self.draw_cen(self.qp)
        self.draw_inter(self.qp)

        self.tunnel(self.qp)

        self.qp.end()


    def tunnel(self,qp):
        qp.setPen(QPen(Qt.GlobalColor.green, 1))

        pnt = MkPoint(0,0)




    def draw_inter(self,qp):

        qp.setPen(QPen(Qt.GlobalColor.cyan, 1))
        
        pnts = []
        pnt = MkPoint(-1.0,-1.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(5.0,5.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(0.5,-1.2)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(0.5,1.2)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(-0.0,0.6)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(-1.0,1.1)
        pnt.conv(self.wtc)
        pnts.append(pnt)


        lines = []
        l = MkLine(pnts[0], pnts[1])
        l.conv(self.wtc)
        lines.append(l)

        l = MkLine(pnts[2], pnts[3])
        l.conv(self.wtc)
        lines.append(l)

        ol = l.offset(1.2,mkDir.mkRIGHT)
        # ol = l.offset(1.2,mkDir.mkLEFT)
        ol.conv(self.wtc)
        lines.append(ol)

        flag0 = l.is_inter(l)
        flag1 = lines[0].is_inter(ol)
        # flag2 = ol.is_inter(lines[0])

        # print(f'line::flag1 {flag1} flag2 {flag2}')

        # p1 = lines[0].get_inter(ol)
        # p2 = ol.get_inter(lines[0])

        # print(f'p1 {p1} p2 {p2}')


        # l = MkLine(pnts[4], pnts[5])
        # l.conv(self.wtc)
        # lines.append(l)

#         # p = lines[3].get_proj(lines[0])
#         # print('######')
#         # print(p)
#         # print('######')
#         lines[3].extend(lines[0])
#         lines[3].conv(self.wtc)
#         #change lines[1], as it is call by reference if the argument is object
#         lines[0].trim(lines[1],mkDir.mkRIGHT)
#         print(lines[1])
#         lines[1].conv(self.wtc)


#         # if lines[0].is_inter(lines[1]):
#         #     print('it is intersected')
#         #     lines[0].calc_lm()
#         #     ipnt = lines[0].get_inter(lines[1])
#         #     print(ipnt)
#         # else:
#         #     print('it is not intersected')
# #--------------------

#         cir = MkCircle()
#         cir.rad = 1.0
#         cir.cen = MkPoint(2,4)
#         cir.conv(self.wtc)
#         cir.draw(self.qp)

#         c2 = cir.offset(1.0,mkDir.mkOUT)
#         # c2.conv(self.wtc)
#         # c2.draw(self.qp)

#         flag1 = c2.is_inter(lines[0])
#         flag2 = lines[0].is_inter(c2)

#         print(f'circle-line::flag1 {flag1} flag2 {flag2}')


#         pnt1, pnt2 = c2.get_inter(lines[0])
#         pnts2 = lines[0].get_inter(c2)

#         print(f'circle-line::pnt1 {pnt1} pnt2 {pnt2}')
#         print(f'circle-line::pnt3 {pnts2[0]} pnt4 {pnts2[1]}')

#         print(f'c2.whang({pnt1}) {c2.whang(pnt1)}')
#         print(f'c2.whang({pnt2}) {c2.whang(pnt2)}')

#         c3 = lines[0].trim(c2,mkDir.mkLEFT)
#         c3.conv(self.wtc)        
#         c3.draw(self.qp)        

#         l1 = l2 = None
#         tag = mkDir.mkOUT | mkDir.mkSTART
#         if c2.trim(lines[0], tag ) is not False:
#             l1, l2 = c2.trim(lines[0], tag)
        
#         lines.pop(0)

#         if l1 is not None: 
#             l1.conv(self.wtc)
#             lines.append(l1)

#         if l2 is not None: 
#             l2.conv(self.wtc)
#             lines.append(l2)

#         for l in lines:
#             l.draw(self.qp)

#         qp.setPen(QPen(Qt.GlobalColor.green, 1))

#         c4 = MkCircle()
#         c4.rad = 2.0
#         c4.cen = MkPoint(0.5,4)
#         c4.conv(self.wtc)
#         c4.draw(self.qp)

#         qp.setPen(QPen(Qt.GlobalColor.red, 1))

#         arc = cir.trim(c4, mkDir.mkIN)
#         arc.conv(self.wtc)
#         arc.draw(self.qp)

#         qp.setPen(QPen(Qt.GlobalColor.blue, 1))
#         arc2 = MkArc()
#         arc2.cen = MkPoint(2.2,3.8)
#         arc2.rad = 2.5
#         arc2.sang = 210
#         arc2.eang = 130+360
#         arc2.conv(self.wtc)
#         arc2.draw(self.qp)


#         arc3 = arc4 = None
#         if arc2.trim(arc,mkDir.mkIN) is not False:
#             print('arc2 trim is not false')
#             arc3, arc4 = arc2.trim(arc,mkDir.mkIN)

#         qp.setPen(QPen(Qt.GlobalColor.white, 1))
#         if arc3 is not None:
#             arc3.conv(self.wtc)
#             arc3.draw(self.qp)
#             print('arc3 drawn')

#         qp.setPen(QPen(Qt.GlobalColor.yellow, 1))
#         if arc4 is not None:
#             arc4.conv(self.wtc)
#             arc4.draw(self.qp)
#             print('arc4 drawn')

#         # n = 2
#         # print(f'line {lines[n]}')    
#         # if lines[n].get_proj(c4) is not False:
#         #     pnt = lines[n].get_proj(c4)
#         #     print(f'line[{n}] get_proj returns pnt {pnt}')
#         #     lines[n].extend(c4)
#         #     lines[n].conv(self.wtc)
#         #     print(f'line[{n}] extended')
#         # else :
#         #     print(f'line[{n}] get_proj returns {lines[n].get_proj(c4)}')    




# #-----------
        

#         # arc = MkArc()
#         # arc.rad = 1.0
#         # arc.cen = MkPoint(2,4)
#         # arc.sang = -4
#         # arc.eang = 180

#         # arc.conv(self.wtc)
#         # arc.draw(self.qp)
#         # print(f'sang {arc.sang} spnt {arc.spnt} eang {arc.eang} epnt {arc.epnt}')

#         # a2 = arc.offset(1.8,mkDir.mkOUT)
#         # a2.conv(self.wtc)
#         # a2.draw(self.qp)

#         # pnt1 = pnt2 = None
#         # pnt3 = pnt4 = None

#         # if a2.get_inter(lines[0]) != False:
#         #     pnt1, pnt2 = a2.get_inter(lines[0])
#         # if lines[0].get_inter(a2) != False:
#         #     pnt3, pnt4 = lines[0].get_inter(a2)

#         # print(f'arc-line::pnt1 {pnt1} pnt2 {pnt2}')
#         # print(f'arc-line::pnt3 {pnt3} pnt4 {pnt4}')

#         # flag = mkDir.mkOUT | mkDir.mkEND # | mkDir.mkSTART

#         # # flag2 = mkDir.mkOUT | mkDir.mkSTART
#         # # print(f'\nflag & {flag2} is {flag2 == flag & flag2} \n')

#         # l1 = l2 = None

#         # if a2.trim(lines[0],flag) is not False:
#         #     l1, l2 = a2.trim(lines[0],flag)
#         #     print('lines 0 is poped')
#         #     lines.pop(0)

#         # if l1 is not None:
#         #     print('l1 is appended')
#         #     l1.conv(self.wtc)
#         #     lines.append(l1)

#         # if l2 is not None:
#         #     print('l2 is appended')
#         #     l2.conv(self.wtc)
#         #     lines.append(l2)        


#         # l = lines[3]
#         # # l.calc_lm()

#         # p1 = l.p1
#         # p2 = l.p2

#         # p3 = MkPoint((p1.x + p2.x)/2, (p1.y + p2.y)/2)
        
#         # print (l, p1, p2, p3)        

#         # t1 = l.get_t(p1)
#         # t2 = l.get_t(p2)
#         # t3 = l.get_t(p3)

#         # print(f't1 {t1} t2 {t2} t3 {t3}')

#         # for l in lines:
#         #     l.draw(self.qp)
        
#         # print('##################\n')
#         # qp.setPen(QPen(Qt.GlobalColor.magenta, 1))        

#         # a4 = MkArc()
#         # a4.rad = 2.0
#         # a4.cen = MkPoint(2,5)
#         # a4.sang = 0
#         # a4.eang = 356
#         # a4.conv(self.wtc)
#         # a4.draw(self.qp)

#         # c5 = MkCircle()
#         # c5.rad = 2.0
#         # c5.cen = MkPoint(1.0,4)
#         # c5.conv(self.wtc)
#         # c5.draw(self.qp)
        
#         # p1 = p2 = None
#         # flag = c5.is_inter(a4)
#         # print(f'intersection of a4 and c5 is {flag}')
#         # if flag is not False:
#         #     p1, p2 = c5.get_inter(a4)  
#         # print(f'intersection points of a4 and c5 are p1 {p1} and p2 {p2}')

#         # n = 1
#         # print(f'line {lines[n]}')    
#         # if lines[n].get_proj(a4) is not False:
#         #     # pnt = lines[n].get_proj(a4)
#         #     # print(f'line[{n}] get_proj returns pnt {pnt}')
#         #     lines[n].extend(a4)
#         #     lines[n].conv(self.wtc)
#         #     lines[n].draw(self.qp)
#         #     print(f'line[{n}] extended')
#         # else :
#         #     print(f'line[{n}] get_proj returns {lines[n].get_proj(a4)}')    


# #-------------------
#         # print(f'dist from p1 to p2 is {pnts[0].dist(pnts[1])}')

#         # pnt = MkPoint(-3,4.555)
#         # pnt.conv(self.wtc)

#         # print(f'dist from l1 to p2 is {lines[0].dist(pnt)}')

#         # print(f'is inter between cir to l1 is {cir.is_inter(lines[0])}')
#         # print(f'is inter between cir to l2 is {cir.is_inter(lines[1])}')

#         # print(f'is in projection range {lines[0].is_in_proj(pnt)}')
#         # print(f'get in projection range {lines[0].get_in_proj(pnt)}')
#         # if cir.get_inter(lines[0]) == False:
#         #     print(f'circle is not intersect with line 0')
#         # else:
#         #     print(f'get inter with circle and line {cir.get_inter(lines[0])}')

#         # x = cir.cen.x+cir.rad*math.cos(0.6)+0.0001
#         # y = cir.cen.y+cir.rad*math.sin(0.6)-0.0001
#         # pnt2 = MkPoint(x,y)
#         # print(f'cir.whang(pnt2) : {cir.whang(pnt2)}')

    def draw_cen(self,qp):
        qp.setPen(QPen(Qt.GlobalColor.red, 1))
        # width = 10
        # height = 10
        # qp.drawArc(self.wtc._cen.x()-width/2,self.wtc._cen.y()-height/2, width, height, 0, 360*16)
        ccir = MkCircle()
        ccir.rad = 0.1
        ccir.cen = MkPoint(0,0)
        ccir.conv(self.wtc)
        ccir.draw(self.qp)

        pnts = []
        pnt = MkPoint(-1.0,.0)
        pnts.append(pnt)

        pnt = MkPoint(1.0,0.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(0.0,-1.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(0.0,1.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        lines = []
        l = MkLine(pnts[0], pnts[1])
        l.conv(self.wtc)
        lines.append(l)
        
        l = MkLine(pnts[2], pnts[3])
        l.conv(self.wtc)
        lines.append(l)

        for l in lines:
            l.draw(self.qp)

    def draw_sc(self, qp):
        qp.setPen(QPen(Qt.GlobalColor.red, 1))

        pnts = []
        pnt = MkPoint(-5.0,5.0)
        pnts.append(pnt)

        pnt = MkPoint(-5.0,0.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(5.0,0.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        pnt = MkPoint(5.0,5.0)
        pnt.conv(self.wtc)
        pnts.append(pnt)

        lines = []
        l = MkLine(pnts[0], pnts[1])
        l.conv(self.wtc)
        lines.append(l)

        l = MkLine(pnts[1], pnts[2])
        l.conv(self.wtc)
        lines.append(l)

        l = MkLine(pnts[2], pnts[3])
        l.conv(self.wtc)
        lines.append(l)

        for l in lines:
            l.draw(self.qp)

        c1 = MkArc()
        c1.cen = MkPoint(0,5)
        c1.rad = 5
        c1.sang = 0*16
        c1.eang = 180*16
        c1.conv(self.wtc)
        c1.draw(self.qp)

    def draw_arc(self, qp):
        qp.setPen(QPen(Qt.GlobalColor.black, 3))
        qp.drawArc(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30°')

        qp.drawArc(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60°')

        qp.drawArc(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90°')

        qp.drawArc(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180°')

        qp.drawArc(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270°')

        qp.drawArc(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360°')

    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)

    def wheelEvent(self, event: QWheelEvent):
        if self.wtc != None:
            
            scale = self.wtc.scale
            scale = scale * math.pow(2,event.angleDelta().y()/120)
            self.wtc.scale = scale
            
            print(f'event.angleDelta().y() {event.angleDelta().y()}, scale {self.wtc.scale} ')
            QWidget.update(self)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        
        self.bcen = self.wtc._cen
        self.mx = a0.x()
        self.my = a0.y()
        txt = f"Mouse 위치 ; x={a0.x()},y={a0.y()}"

        print(txt)
        return super().mousePressEvent(a0)

    def mouseMoveEvent(self, a0):
        super().mouseMoveEvent(a0)

        dx = a0.x() - self.mx
        dy = a0.y() - self.my
        
        self.wtc._cen = QPoint(self.bcen.x()+dx, self.bcen.y()+dy)

        QWidget.update(self)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        
        dx = a0.x() - self.mx
        dy = a0.y() - self.my

        self.wtc._cen = QPoint(self.bcen.x()+dx, self.bcen.y()+dy)
        QWidget.update(self)

        return super().mouseReleaseEvent(a0)


def main():
    app = QApplication(sys.argv)

    # w = QWidget()
    # p = w.palette()
    # p.setColor(w.backgroundRole(), Qt.GlobalColor.red)
    # w.setPalette(p)

    ex = MyApp()
    sys.exit(app.exec())


if __name__=="__main__":
    main()


