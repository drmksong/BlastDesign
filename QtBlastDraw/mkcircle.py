from mklib import *
import copy

class MkCircle(MkObj):
    def __init__(self, parent=None):
        super().__init__()
        self.classname = 'MkCircle'
        self._qcen = QPoint(0,0)
        self._qrad = 0
        self._cen = MkPoint(0,0)
        self._rad = 0
        self.isconv = False

    def get_pnt(self, ang: float) -> MkPoint:
        return MkPoint(self.cen.x + self.rad*math.cos(ang*math.pi/180),
                       self.cen.y + self.rad*math.sin(ang*math.pi/180))

    # angle is always in degree, to be used for math functions it needs to be converted in rad
    def whang(self,pnt:MkPoint) -> float:
        dx = pnt.x - self.cen.x
        dy = pnt.y - self.cen.y

        if abs(math.sqrt(dx*dx+dy*dy) - self.rad) > EPS:
            print(f'abs(math.sqrt(dx*dx+dy*dy) - self.rad) {abs(math.sqrt(dx*dx+dy*dy) - self.rad)}')
            return False
        
        if abs(dx) < EPS:
            if dy > 0: 
                ang = 90*math.pi/180 
            elif dy < 0:
                ang = 270*math.pi/180
            return ang*180/math.pi

        ang = math.atan2(dy,dx)
        if ang < 0:
            ang = ang + 2*math.pi

        if ang > 2*math.pi:
            ang = ang - 2*math.pi

        return ang*180/math.pi


    # is_along is to check whether the point is on the trace of circle 
    def is_along(self, p:MkPoint) -> bool:
        d = self._cen.dist(p)
        if abs(d-self._rad) < EPS:
            return True
        else:
            return False

    # is_in is to check whether the point is on the trace of circle 
    def is_in(self, p:MkPoint) -> bool:
        d = self._cen.dist(p)
        if d < self._rad:
            return True
        else:
            return False

    # it is to check whether the extention of the line inter with circle
    # it should be further checked the segment of the line, i.e. t is within 0.0 to 1.0
    @dispatch
    def is_inter(self, line:MkLine)->bool:
        x1 = line._p1.x
        y1 = line._p1.y
        xc = self._cen.x
        yc = self._cen.y

        l = line.l
        m = line.m 

        lc = x1 - xc
        mc = y1 - yc

        r = self._rad

        a = (l*l + m*m)
        b = 2*(l*lc + m*mc)
        c = lc*lc + mc*mc - r*r

        if b*b - 4*a*c < 0:
            print( f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}')
            return False
        else:
            return True
    
    @dispatch
    def get_inter(self, line:MkLine):
        # flag = self.is_inter(line)
        # if flag == False:
        #     return flag

        x1 = line._p1.x
        y1 = line._p1.y
        xc = self._cen.x
        yc = self._cen.y

        l = line.l
        m = line.m 

        lc = x1 - xc
        mc = y1 - yc

        r = self._rad

        a = (l*l + m*m)
        b = 2*(l*lc + m*mc)
        c = lc*lc + mc*mc - r*r

        # it is not assert item as the condition can happen when line is out of circle
        # assert b*b - 4*a*c > 0, f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}'

        if b*b - 4*a*c < 0:
            print( f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}')
            return False

        t1 = (-b+math.sqrt(b*b-4*a*c))/2/a
        t2 = (-b-math.sqrt(b*b-4*a*c))/2/a

        pnt1 = line.get_p(t1) if 0 <= t1 and t1 <= 1 else None
        pnt2 = line.get_p(t2) if 0 <= t2 and t2 <= 1 else None

        return (pnt1, pnt2)

    @dispatch
    def is_inter(self, c:'MkCircle')->bool:
        d = self._cen.dist(c._cen)
        print(f'd {d} self.rad {self.rad} c.rad {c.rad}')
        if d < self._rad + c._rad:
            return True
        else:
            return False

    @dispatch
    def get_inter(self, c:'MkCircle'):
        if self.is_inter(c) == False:
            print(f'#### circle :: return false')            
            return False

        x1 = self.cen.x
        x2 = c.cen.x

        y1 = self.cen.y
        y2 = c.cen.y

        r1 = self.rad
        r2 = c.rad

        d = c.cen.dist(self.cen)
        l = (r1*r1-r2*r2+d*d)/2/d
        print(f'#### circle :: d {d} l {l} r1 {r1} r2 {r2}')
        if (r1*r1-l*l<0):
            return False

        h = math.sqrt(r1*r1-l*l)

        x3 = l/d*(x2-x1) + h/d*(y2-y1)+x1
        y3 = l/d*(y2-y1) - h/d*(x2-x1)+y1

        x4 = l/d*(x2-x1) - h/d*(y2-y1)+x1
        y4 = l/d*(y2-y1) + h/d*(x2-x1)+y1

        p3 = MkPoint(x3,y3)
        p4 = MkPoint(x4,y4)
        return (p3,p4)


    # is_inter between circle and arc is to check circle and arc's circle
    # is overlapped and if two intersections are in arc return true else return false
    # TODO : write test code
    @dispatch
    def is_inter(self, a:'MkArc') -> bool:
        d = self._cen.dist(a._cen)
        if d > self._rad + a._rad:
            print('distance is far')
            return False

        c = MkCircle()
        c.rad = a.rad
        c.cen = a.cen
        
        if self.get_inter(c) is False:
            print('get_inter is false')
            return False

        p1,p2 = self.get_inter(c)

        ang1 = a.whang(p1)
        ang2 = a.whang(p2)

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (a.sang < ang1     and ang1 < a.eang) or \
           (a.sang+360 < ang1 and ang1 < a.eang+360) or \
           (a.sang-360 < ang1 and ang1 < a.eang-360):
            flag1 = True

        if (a.sang < ang2     and ang2 < a.eang) or \
           (a.sang+360 < ang2 and ang2 < a.eang+360) or \
           (a.sang-360 < ang2 and ang2 < a.eang-360):
            flag2 = True
       
        return flag1 or flag2


    # TODO : write test code 
    @dispatch
    def get_inter(self, a:'MkArc'):
        if self.is_inter(a) == False:
            print(f'#### arc :: return false')            
            return False

        # at least there is one intersection point 

        c = MkCircle()
        c.rad = a.rad
        c.cen = a.cen

        p1,p2 = self.get_inter(c)

        ang1 = a.whang(p1) if p1 is not None else None
        ang2 = a.whang(p2) if p2 is not None else None

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (a.sang < ang1     and ang1 < a.eang) or \
           (a.sang+360 < ang1 and ang1 < a.eang+360) or \
           (a.sang-360 < ang1 and ang1 < a.eang-360):
            flag1 = True

        if (a.sang < ang2     and ang2 < a.eang) or \
           (a.sang+360 < ang2 and ang2 < a.eang+360) or \
           (a.sang-360 < ang2 and ang2 < a.eang-360):
            flag2 = True
       
        if flag1 == False and flag2 == False:
            return False

        p3 = p1 if ang1 is not None and flag1 else None
        p4 = p2 if ang2 is not None and flag2 else None

        return (p3,p4)


    # how we define the distance to the circle
    # shortest distance from the point to circle
    @dispatch
    def dist(self, p:MkPoint) -> float:
        d = self._cen.dist(p)
        return max(d - self._rad, 0)

    # how we define the distance to the circle
    # shortest distance from the line to circle
    @dispatch
    def dist(self, l:MkLine) -> float:
        d = l.dist(self._cen)
        return abs(d - self._rad, 0)

    # how we define the distance to the circle
    # shortest distance from the circle to circle
    @dispatch
    def dist(self, c:'MkCircle') -> float:
        d = self._cen.dist(c._cen)
        return max(d - self._rad - c._rad, 0)

    # TODO : write code
    @dispatch
    def dist(self, a:'MkArc') -> float:
        raise Exception('NotYetImplement') 

    @dispatch
    def offset(self, dist: float, dir : mkDir) -> 'MkCircle':
        c = MkCircle()
        c.cen = self.cen
        c.rad = self.rad + dist if dir is mkDir.mkOUT else -dist
        return c
    
    # cut the line l with self circle
    # TODO : write test code 
    @dispatch
    def trim(self, l: MkLine, dir: mkDir):
                
        p = MkPoint(0,0)
        p2 = MkPoint(0,0.001)
        line1 = MkLine(p,p2)
        line2 = MkLine(p,p2)

        spnt = l.p1
        epnt = l.p2

        if self.get_inter(l) == False:
            return False

        pnt1, pnt2 = self.get_inter(l) 

        flag = pnt1 != None and pnt2 != None # two points then true, one or less then false

        assert pnt1 is not None or pnt2 is not None, f'MkCircle::trim with line, it is strange pnt1 {pnt1} and pnt2 {pnt2}'

        print(f' mkIN is {dir}')

        if (dir & mkDir.mkIN) == mkDir.mkIN:
            assert flag, f'MkArc::trim with line, it is strange dir is mkIN but intersections should be two pnts' 
            assert (dir & mkDir.mkSTART) is not mkDir.mkSTART and \
                   (dir & mkDir.mkEND) is not mkDir.mkEND , \
                   f'MkArc::trim with line, mkIN should not come with mkSTART or mkEND'
    
        if mkDir.mkIN == (dir & mkDir.mkIN) and flag:
            line1.p1 = spnt
            line1.p2 = pnt1 if spnt.dist(pnt1) < spnt.dist(pnt2) else pnt2

            line2.p1 = pnt1 if epnt.dist(pnt1) < epnt.dist(pnt2) else pnt2
            line2.p2 = epnt

            print('mkIN selected')

        if flag: # two intersection points 
            if (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART):
                line1.p1 = pnt1
                line1.p2 = pnt2
                line2 = None               
                print('mkOUT and mkEND and mkSTART selected')
            
            elif (mkDir.mkOUT | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkSTART):
                line1.p1 = pnt1 if epnt.dist(pnt1) > epnt.dist(pnt2) else pnt2
                line1.p2 = epnt
                line2 = None

                print('mkOUT and mkSTART selected')
                
            elif (mkDir.mkOUT | mkDir.mkEND) == dir & (mkDir.mkOUT | mkDir.mkEND):
                line1 = None
                line2.p1 = spnt
                line2.p2 = pnt1 if spnt.dist(pnt1) > spnt.dist(pnt2) else pnt2

                print('mkOUT and mkEND selected')

            elif (mkDir.mkOUT) == dir & (mkDir.mkOUT): # default trim two sides of the arc
                line1.p1 = pnt1
                line1.p2 = pnt2
                line2 = None               

                print('mkOUT selected')

        elif pnt1 is not None and pnt2 is None: 
            if (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART):
                line1 = None               
                line2 = None               
                print('mkOUT and mkEND and mkSTART selected')
            
            elif (mkDir.mkOUT | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkSTART):
                line1.p1 = spnt
                line1.p2 = pnt1
                line2 = None
                print('mkOUT and mkSTART selected')
                
            elif (mkDir.mkOUT | mkDir.mkEND) == dir & (mkDir.mkOUT | mkDir.mkEND):
                line1 = None
                line2.p1 = pnt1
                line2.p2 = epnt
                print('mkOUT and mkEND selected')

            elif (mkDir.mkOUT) == dir & (mkDir.mkOUT): # default trim two sides of the arc
                line1 = None               
                line2 = None               
                print('mkOUT selected')
            

        elif pnt1 is None and pnt2 is not None:
            if (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkEND | mkDir.mkSTART):
                line1 = None               
                line2 = None               
                print('mkOUT and mkEND and mkSTART selected')
            
            elif (mkDir.mkOUT | mkDir.mkSTART) == dir & (mkDir.mkOUT | mkDir.mkSTART):
                line1.p1 = spnt
                line1.p2 = pnt2
                line2 = None
                print('mkOUT and mkSTART selected')
                
            elif (mkDir.mkOUT | mkDir.mkEND) == dir & (mkDir.mkOUT | mkDir.mkEND):
                line1 = None
                line2.p1 = pnt2
                line2.p2 = epnt
                print('mkOUT and mkEND selected')

            elif (mkDir.mkOUT) == dir & (mkDir.mkOUT): # default trim two sides of the arc
                line1 = None               
                line2 = None               
                print('mkOUT selected')

        return (line1, line2)



    # cut the circle c with self circle
    # dir is only mkDir.mkIN or mkDir.mkOut, no left, right, start and end
    # TODO : write test code 
    @dispatch
    def trim(self, c: 'MkCircle', dir: mkDir):
        from mkarc import MkArc
        if self.is_inter(c) is False:
            return False

        p1, p2 = self.get_inter(c)

        assert p1 is not None and p2 is not None, f'MkCircle::trim circle ~ it is strange p1 {p1} p2 {p2}'

        a1 = c.whang(p1)
        a2 = c.whang(p2)

        amid = (a1+a2)/2
        pmid = c.get_pnt(amid)

        flag = mkDir.mkNONE

        flag = mkDir.mkIN if self.is_in(pmid) is True else mkDir.mkOUT

        a = MkArc()
        a.cen = c.cen
        a.rad = c.rad

        # TODO : need to check if dir is in or out and assign sang a1 or a2 based on dir

        if dir is mkDir.mkIN and flag is mkDir.mkIN:
            print(f'mid point is {pmid}  a1 {a1} a2 {a2} dir {dir} flag {flag}')
            a.sang = max(a1,a2)
            a.eang = min(a1,a2) + 360
        elif dir is mkDir.mkOUT and flag is mkDir.mkOUT:
            print(f'mid point is {pmid}  a1 {a1} a2 {a2} dir {dir} flag {flag}')
            a.sang = max(a1,a2)
            a.eang = min(a1,a2) + 360
        elif dir is mkDir.mkIN and flag is mkDir.mkOUT:
            print(f'mid point is {pmid}  a1 {a1} a2 {a2} dir {dir} flag {flag}')
            a.sang = min(a1,a2)
            a.eang = max(a1,a2)
        elif dir is mkDir.mkOUT and flag is mkDir.mkIN:
            print(f'mid point is {pmid}  a1 {a1} a2 {a2} dir {dir} flag {flag}')
            a.sang = min(a1,a2)
            a.eang = max(a1,a2)

        return a

        
    # cut the arc a with self circle
    # TODO : write test code 
    @dispatch
    def trim(self, arc: 'MkArc', dir: mkDir):
        from mkarc import MkArc
        if self.is_inter(arc) is False:
            return False

        p1, p2 = self.get_inter(arc)

        if p1 is None and p2 is None:
            return False

        ang1 = arc.whang(p1) if p1 is not None else None
        ang2 = arc.whang(p2) if p2 is not None else None

        print(f'**** mkcircle::trim with arc, p1 {p1} ang1 {ang1} p2 {p2} ang2 {ang2}')        

        if p1 is not None and p2 is not None:        

            amid = (ang1+ang2)/2
            pmid = arc.get_pnt(amid) # pmid can be out of arc, along the base circle

            flag = mkDir.mkNONE

            flag = mkDir.mkIN if self.is_in(pmid) is True else mkDir.mkOUT

            arc1 = copy.deepcopy(arc)

            arc2 = copy.deepcopy(arc)


            # TODO : need to check if dir is in or out and assign sang a1 or a2 based on dir

            if dir is mkDir.mkIN and flag is mkDir.mkIN:
                print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
                arc1.sang = arc.sang
                arc1.eang = min(ang1,ang2)
                arc2.sang = max(ang1,ang2)
                arc2.eang = arc.eang
    
            elif dir is mkDir.mkIN and flag is mkDir.mkOUT:
                print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
                arc1.sang = min(ang1,ang2)
                arc1.eang = max(ang1,ang2)
                arc2 = None

            elif dir is mkDir.mkOUT and flag is mkDir.mkIN:
                print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
                arc1.sang = min(ang1,ang2)
                arc1.eang = max(ang1,ang2)
                arc2 = None
            elif dir is mkDir.mkOUT and flag is mkDir.mkOUT:
                print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
                arc1.sang = arc.sang
                arc1.eang = min(ang1,ang2)
                arc2.sang = max(ang1,ang2)
                arc2.eang = arc.eang

            return arc1, arc2

        elif p1 is not None or p2 is not None:

            flag = mkDir.mkIN if self.is_in(arc.spnt) is True else mkDir.mkOUT

            a = copy.deepcopy(arc)

            # TODO : need to check if dir is in or out and assign sang a1 or a2 based on dir

            ang = ang1 if ang1 is not None else ang2

            if dir is mkDir.mkIN and flag is mkDir.mkIN:
                a.sang = min(arc.eang,ang)
                a.eang = max(arc.eang,ang)
            elif dir is mkDir.mkOUT and flag is mkDir.mkIN:
                a.sang = min(arc.sang,ang)
                a.eang = max(arc.sang,ang)
            elif dir is mkDir.mkIN and flag is mkDir.mkOUT:
                a.sang = min(arc.sang,ang)
                a.eang = max(arc.sang,ang)
            elif dir is mkDir.mkOUT and flag is mkDir.mkOUT:
                a.sang = min(arc.eang,ang)
                a.eang = max(arc.eang,ang)

            return a, None


        

    @property
    def cen(self):
        return self._cen

    @cen.setter
    def cen(self,_cen):
        self._cen = _cen
        self.isconv = False

    @property
    def rad(self):
        return self._rad

    @rad.setter
    def rad(self,_rad):
        self._rad = _rad
        self.isconv = False
    
    def conv(self, wtc: WorldToCanvas):
        self._qcen = self._cen.conv(wtc)
        self._qrad = self._rad*wtc.scale
        self.isconv = True

    def draw(self, qp):
        # qp.drawArc(self._qcen.x()-self._qrad,self._qcen.y()-self._qrad, self._qrad*2, self._qrad*2, 0, 360*16)
        qp.drawArc(int(self._qcen.x()-self._qrad),int(self._qcen.y()-self._qrad), int(self._qrad*2), int(self._qrad*2), 0, 360*16)        
    def __repr__(self):
        return f"MkCircle({self._cen}, {self._rad}, isconv {self.isconv})"
