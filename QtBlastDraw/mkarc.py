from mklib import *
import copy

class MkArc(MkCircle):
    def __init__(self,parent=None):
        super().__init__()
        self.classname = 'MkArc'
        self._sang = 0 # in degree
        self._eang = 0 # in degree

    @property
    def spnt(self):
        x = self.cen.x + self.rad*math.cos(self.sang*math.pi/180)
        y = self.cen.y + self.rad*math.sin(self.sang*math.pi/180)
        return MkPoint(x,y)

    @property
    def epnt(self):
        x = self.cen.x + self.rad*math.cos(self.eang*math.pi/180)
        y = self.cen.y + self.rad*math.sin(self.eang*math.pi/180)
        return MkPoint(x,y)

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

        t1 = (-b+math.sqrt(b*b-4*a*c))/2/a
        t2 = (-b-math.sqrt(b*b-4*a*c))/2/a

        pnt1 = line.get_p(t1)
        pnt2 = line.get_p(t2)

        # print(f'type of self.whang(pnt1) {type(self.whang(pnt1))}')
        # print(f'{self.whang(pnt1)} == False {self.whang(pnt1) == False}')
        # print(f'self.whang({pnt2}) == False {self.whang(pnt2) == False}')

        assert type(self.whang(pnt1)) != bool and type(self.whang(pnt2)) != bool, f'MkArc::is_inter angle check failed pnt1 {self.whang(pnt1)} pnt2 {self.whang(pnt2)}'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = self.whang(pnt1)
        ang2 = self.whang(pnt2)

        # print(f'MkAng::is_inter ang1 {ang1} ang2 {ang2}')

        # either of two points is within the arc, then return true as it is intersected with line anyway
        if self.sang < ang1 and ang1 < self.eang:
            return True

        if self.sang < ang2 and ang2 < self.eang:
            return True

        # if none of two points is within the arc, then return false as it is not intersected
        return False

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

        pnt1 = line.get_p(t1)
        pnt2 = line.get_p(t2)

        assert type(self.whang(pnt1)) != bool and type(self.whang(pnt2)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = self.whang(pnt1)
        ang2 = self.whang(pnt2)

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (self.sang < ang1     and ang1 < self.eang) or \
           (self.sang+360 < ang1 and ang1 < self.eang+360) or \
           (self.sang-360 < ang1 and ang1 < self.eang-360):
            flag1 = True

        if (self.sang < ang2     and ang2 < self.eang) or \
           (self.sang+360 < ang2 and ang2 < self.eang+360) or \
           (self.sang-360 < ang2 and ang2 < self.eang-360):
            flag2 = True
       
        if flag1 == False and flag2 == False:
            return False

        # either of two points is within the arc, then return true as it is intersected with line anyway
        
        p1 = pnt1 if 0 <= t1 and t1 <= 1 and flag1 else None
        p2 = pnt2 if 0 <= t2 and t2 <= 1 and flag2 else None

        return (p1,p2) #(pnt1, pnt2)

    # TODO : write test code
    @dispatch
    def is_inter(self, cir:MkCircle)->bool:
        d = self._cen.dist(cir._cen)
        if d > self._rad + cir._rad:
            print('distance is far')
            return False

        c = MkCircle()
        c.rad = self.rad
        c.cen = self.cen
        
        if cir.get_inter(c) is False:
            print('MkArc::get_inter with circle is false')
            return False

        p1,p2 = cir.get_inter(c)

        ang1 = self.whang(p1)
        ang2 = self.whang(p2)

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (self.sang < ang1     and ang1 < self.eang) or \
           (self.sang+360 < ang1 and ang1 < self.eang+360) or \
           (self.sang-360 < ang1 and ang1 < self.eang-360):
            flag1 = True

        if (self.sang < ang2     and ang2 < self.eang) or \
           (self.sang+360 < ang2 and ang2 < self.eang+360) or \
           (self.sang-360 < ang2 and ang2 < self.eang-360):
            flag2 = True
       
        return flag1 or flag2

    # TODO : write test code, concerning reciprocal call issue
    @dispatch
    def get_inter(self, c:MkCircle):
        if self.is_inter(c) == False:
            return False

        x1 = self._cen.x
        x2 = c._cen.x

        y1 = self._cen.y
        y2 = c._cen.y

        r1 = self._rad
        r2 = c._rad

        d = c._cen.dist(self._cen)
        l = (r1*r1-r2*r2+d*d)/2/d

        if (r1*r1-l*l<0):
            return False

        h = math.sqrt(r1*r1-l*l)

        x3 = l/d*(x2-x1) + h/d*(y2-y1)+x1
        y3 = l/d*(y2-y1) - h/d*(x2-x1)+y1

        x4 = l/d*(x2-x1) - h/d*(y2-y1)+x1
        y4 = l/d*(y2-y1) + h/d*(x2-x1)+y1

        p3 = MkPoint(x3,y3)
        p4 = MkPoint(x4,y4)

        # the points p3, and p4 should be along the arc
        assert type(self.whang(p3)) != bool and type(self.whang(p4)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = self.whang(p3)
        ang2 = self.whang(p4)

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (self.sang < ang1     and ang1 < self.eang) or \
           (self.sang+360 < ang1 and ang1 < self.eang+360) or \
           (self.sang-360 < ang1 and ang1 < self.eang-360):
            flag1 = True

        if (self.sang < ang2     and ang2 < self.eang) or \
           (self.sang+360 < ang2 and ang2 < self.eang+360) or \
           (self.sang-360 < ang2 and ang2 < self.eang-360):
            flag2 = True
       
        if flag1 == False and flag2 == False:
            return False

        # either of two points is within the arc, then return true as it is intersected with line anyway
        
        p3 = p3 if flag1 else None
        p4 = p3 if flag2 else None

        return (p3,p4)

    # TODO : write code
    @dispatch
    def is_inter(self, a:'MkArc')->bool:
        d = self._cen.dist(a._cen)
        if d > self._rad + a._rad:
            print('distance is far')
            return False

        ca = MkCircle()
        ca.rad = a.rad
        ca.cen = a.cen

        cs = MkCircle()
        cs.rad = self.rad
        cs.cen = self.cen
        
        if cs.get_inter(ca) is False:
            print('get_inter is false')
            return False

        p1,p2 = ca.get_inter(cs)

        ang1 = ca.whang(p1)
        ang2 = ca.whang(p2)

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

        ang3 = cs.whang(p1)
        ang4 = cs.whang(p2)

        flag3 = flag3 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (self.sang     < ang3 and ang3 < self.eang) or \
           (self.sang+360 < ang3 and ang3 < self.eang+360) or \
           (self.sang-360 < ang3 and ang3 < self.eang-360):
            flag3 = True

        if (self.sang     < ang4 and ang4 < self.eang) or \
           (self.sang+360 < ang4 and ang4 < self.eang+360) or \
           (self.sang-360 < ang4 and ang4 < self.eang-360):
            flag4 = True


        return (flag1 and flag3) or (flag2 and flag4)
        

    # TODO : write test code
    @dispatch
    def get_inter(self, a:'MkArc'):
        if self.is_inter(a) == False:
            return False

        x1 = self._cen.x
        x2 = a._cen.x

        y1 = self._cen.y
        y2 = a._cen.y

        r1 = self._rad
        r2 = a._rad

        d = a._cen.dist(self._cen)
        l = (r1*r1-r2*r2+d*d)/2/d

        if (r1*r1-l*l<0):
            return False

        h = math.sqrt(r1*r1-l*l)

        x3 = l/d*(x2-x1) + h/d*(y2-y1)+x1
        y3 = l/d*(y2-y1) - h/d*(x2-x1)+y1

        x4 = l/d*(x2-x1) - h/d*(y2-y1)+x1
        y4 = l/d*(y2-y1) + h/d*(x2-x1)+y1

        p3 = MkPoint(x3,y3)
        p4 = MkPoint(x4,y4)

        assert type(self.whang(p3)) != bool and type(self.whang(p4)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = self.whang(p3)
        ang2 = self.whang(p4)

        flag1 = flag2 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (self.sang < ang1     and ang1 < self.eang) or \
           (self.sang+360 < ang1 and ang1 < self.eang+360) or \
           (self.sang-360 < ang1 and ang1 < self.eang-360):
            flag1 = True

        if (self.sang < ang2     and ang2 < self.eang) or \
           (self.sang+360 < ang2 and ang2 < self.eang+360) or \
           (self.sang-360 < ang2 and ang2 < self.eang-360):
            flag2 = True
       
        if flag1 == False and flag2 == False:
            return False

        ang3 = a.whang(p3)
        ang4 = a.whang(p4)

        flag3 = flag4 = False

        # TODO : This code is bug prone, must revise it to resilient code
        if (a.sang <     ang3 and ang3 < a.eang) or \
           (a.sang+360 < ang3 and ang3 < a.eang+360) or \
           (a.sang-360 < ang3 and ang3 < a.eang-360):
            flag3 = True

        if (a.sang <     ang4 and ang4 < a.eang) or \
           (a.sang+360 < ang4 and ang4 < a.eang+360) or \
           (a.sang-360 < ang4 and ang4 < a.eang-360):
            flag4 = True
       
        if flag3 == False and flag4 == False:
            return False

        # either of two points is within the arc, then return true as it is intersected with line anyway
        
        p3 = p3 if flag1 and flag3 else None
        p4 = p4 if flag2 and flag4 else None

        return (p3,p4)

    # TODO : write test code of this function thoroughly
    # if the point is in the circle of arc, then it returns false
    # if the point is outside of the arc or outside of circle, then it finds 
    # the intersection of the the line from the point to the center, and then if
    # the intersection point is on the arc, then dist if from the point 
    # to the intersection point, otherwise, check which is the nearest end point
    @dispatch
    def dist(self, p:MkPoint) -> float:
        if self.is_in(p):
            return False

        l = MkLine(p,self._cen)
        len = l.Len

        if self.get_inter(l) != False:
            pnt1, pnt2  = self.get_inter(l)

        assert pnt1 is not None or pnt2 is not None, 'MkArc::dist wrt point, both points are None'

        d1 = p.dist(pnt1) if pnt1 is not None else None
        d2 = p.dist(pnt2) if pnt2 is not None else None
        d3 = p.dist(self.spnt())
        d4 = p.dist(self.epnt())

        dl = [d1,d2,d3,d4]
        
        mindis = min(d for d in dl if d is not None)

        return mindis

    # TODO : write test code of this function thoroughly
    @dispatch
    def dist(self, l:MkLine) -> float:
        if self.is_inter(l):
            return False

        pp = l.get_proj(self.cen)
        lp = MkLine(self.cen,pp)

        if self.get_inter(lp) is not False:
            pnt1, pnt2  = self.get_inter(lp)

        assert pnt1 is not None or pnt2 is not None, 'MkArc::dist wrt line, both points are None'

        d1 = l.dist(pnt1) if pnt1 is not None else None
        d2 = l.dist(pnt2) if pnt2 is not None else None
        d3 = l.dist(self.spnt())
        d4 = l.dist(self.epnt())

        dl = [d1,d2,d3,d4]
        
        mindis = min(d for d in dl if d is not None)

        return mindis

    # TODO : write code
    @dispatch
    def dist(self, c:MkCircle) -> float:
        pass

    # TODO : write code 
    def dist(self, a:'MkArc') -> float:
        pass

    def offset(self, dist: float, dir : mkDir) -> 'MkArc':
        a = MkArc()
        a.cen = self.cen
        a.rad = self.rad + dist if dir is mkDir.mkOUT else -dist
        a.sang = self.sang
        a.eang = self.eang
        return a
    
    # TODO : write test code and check meaning of changing l as well as returning l as line 1 
    # cut line with self arc
    @dispatch
    def trim(self, l: MkLine, dir:mkDir):
                
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

        assert pnt1 != None or pnt2 != None, f'MkArc::trim with line, it is strange both pnt1 {pnt1} and pnt2 {pnt2}'

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

    # TODO : write test code 
    @dispatch
    def trim(self, cir: MkCircle, dir:mkDir):

        if cir.is_inter(self) is False:
            return False

        p1, p2 = cir.get_inter(self)

        # if any of the these is None return false
        if p1 is None or p2 is None:
            return False

        # both points are valid intersection points

        ang1 = cir.whang(p1) if p1 is not None else None
        ang2 = cir.whang(p2) if p2 is not None else None

        print(f'**** mkarc::trim with circle, p1 {p1} ang1 {ang1} p2 {p2} ang2 {ang2}')        

        amid = (ang1+ang2)/2
        pmid = cir.get_pnt(amid) # pmid can be out of arc, along the base circle

        flag = mkDir.mkNONE

        flag = mkDir.mkIN if self.is_in(pmid) is True else mkDir.mkOUT

        arc = MkArc()
        arc.cen = cir.cen
        arc.rad = cir.rad

        # TODO : need to check if dir is in or out and assign sang a1 or a2 based on dir

        if dir is mkDir.mkIN and flag is mkDir.mkIN:
            print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
            arc.sang = max(ang1,ang2)
            arc.eang = min(ang1,ang2) + 360

        elif dir is mkDir.mkOUT and flag is mkDir.mkIN:
            print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
            arc.sang = min(ang1,ang2)
            arc.eang = max(ang1,ang2)

        elif dir is mkDir.mkIN and flag is mkDir.mkOUT:
            print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
            arc.sang = min(ang1,ang2)
            arc.eang = max(ang1,ang2)

        elif dir is mkDir.mkOUT and flag is mkDir.mkOUT:
            print(f'mid point is {pmid}  a1 {ang1} a2 {ang2} dir {dir} flag {flag}')
            arc.sang = max(ang1,ang2)
            arc.eang = min(ang1,ang2) + 360

        return arc, None


    # TODO : write code 
    @dispatch
    def trim(self, arc: 'MkArc', dir:mkDir):
        
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
    def sang(self):
        return self._sang

    @sang.setter
    def sang(self, _sang):
        self._sang = _sang

    @property
    def eang(self):
        return self._eang

    @eang.setter
    def eang(self, _eang):
        self._eang = _eang

    def conv(self, wtc:WorldToCanvas):
        super().conv(wtc)

    def draw(self, qp):
        # qp.drawArc(self._qcen.x()-self._qrad,self._qcen.y()-self._qrad, self._qrad*2, self._qrad*2, self._sang*16, (self._eang-self._sang)*16)        
        qp.drawArc(int(self._qcen.x()-self._qrad),int(self._qcen.y()-self._qrad), int(self._qrad*2), int(self._qrad*2), int(self._sang*16), int((self._eang-self._sang)*16))        
    def __repr__(self):
        return f"MkArc({self._cen}, {self._rad}, isconv {self.isconv})"

