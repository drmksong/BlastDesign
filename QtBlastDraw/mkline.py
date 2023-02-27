from mklib import *

class MkLine(MkObj):
    def __init__(self,p1:MkPoint,p2:MkPoint, parent=None):
        super().__init__()
        self.classname = 'MkLine'
        self._qline = QLine(QPoint(0,0),QPoint(0,0))
        self._p1 : MkPoint = p1
        self._p2 : MkPoint = p2
        self.l = 0    # (x - p1.x) / (p2.x - p1.x) = (y - p1.y) / (p2.y - p1.y)
        self.m = 0    # (x - p1.x) / l = (y - p1.y) / m  -> l,m is unit vector
        self.A = 0
        self.B = 0
        self.C = 0
        self.Len = p1.dist(p2)
        
        self.calc_lm()
        self.isconv = False
        
    def calc_lm(self):
        x1 = self._p1.x
        x2 = self._p2.x
        y1 = self._p1.y
        y2 = self._p2.y

        L = x2 - x1
        M = y2 - y1

        assert abs(L) > EPS or abs(M) > EPS, f'MkLine::calc_lm() L { L } or M {M} should not be zero'

        if abs(L) < EPS:
          self.A = -1
          self.B = 0
          self.C = x1

        elif abs(M) < EPS:
          self.A = 0
          self.B = -1
          self.C = y1

        else:
          a = M/L
          self.A = -a
          self.B = 1
          self.C = a*x1 - y1

        LM = math.sqrt(L*L+M*M)
        self.l = L#/LM
        self.m = M#/LM
        self.Len = self.p1.dist(self.p2)
          
      
    def get_p(self,t:float) -> MkPoint:
      x = self._p1.x + t*self.l
      y = self._p1.y + t*self.m
      return MkPoint(x,y)

    # TODO : write test code
    def get_t(self,p:MkPoint) -> float:

      assert abs(self.l) > EPS or abs(self.m) > EPS, f'either l {self.l} or m {self.m} should not be zero'
      
      if abs(self.l) < EPS:
        tx = ty = (p.y-self.p1.y) /self.m

      elif abs(self.m) < EPS:
        ty = tx = (p.x-self.p1.x) /self.l

      else:
        tx = (p.x-self.p1.x) /self.l
        ty = (p.y-self.p1.y) /self.m

      if abs(tx-ty) > EPS:
        return False

      return (tx+ty)/2


    # only if the two line segments are intersected with each other
    @dispatch
    def is_inter(self, line:'MkLine') -> bool: 
      x1 = self._p1.x
      x2 = self._p2.x
      x3 = line._p1.x
      x4 = line._p2.x

      y1 = self._p1.y
      y2 = self._p2.y
      y3 = line._p1.y
      y4 = line._p2.y

      assert abs(x1-x2) > EPS or abs(y1-y2) > EPS
      assert abs(x3-x4) > EPS or abs(y3-y4) > EPS

      t34_u = ((x1-x3)*(y2-y1) - (y1-y3)*(x2-x1)) 
      t34_d = ((x4-x3)*(y2-y1) - (y4-y3)*(x2-x1))
      
      assert abs(t34_d) > EPS

      t34 = t34_u / t34_d

      t12_u = ((x1-x3)*(y4-y3) - (y1-y3)*(x4-x3)) 
      t12_d = ((x2-x1)*(y4-y3) - (y2-y1)*(x4-x3))

      assert abs(t12_d) > EPS

      t12 = - t12_u / t12_d

      return (0 <= t12 and t12 <= 1) and (0 <= t34  and t34 <= 1)

    @dispatch
    def get_inter(self, line:'MkLine') -> MkPoint:
      x1 = self._p1.x
      x2 = self._p2.x
      x3 = line._p1.x
      x4 = line._p2.x

      y1 = self._p1.y
      y2 = self._p2.y
      y3 = line._p1.y
      y4 = line._p2.y

      assert abs(x1-x2) > EPS or abs(y1-y2) > EPS
      assert abs(x3-x4) > EPS or abs(y3-y4) > EPS

      t34_u = ((x1-x3)*(y2-y1) - (y1-y3)*(x2-x1)) 
      t34_d = ((x4-x3)*(y2-y1) - (y4-y3)*(x2-x1))
      
      assert abs(t34_d) > EPS

      t34 = t34_u / t34_d

      t12_u = ((x1-x3)*(y4-y3) - (y1-y3)*(x4-x3)) 
      t12_d = ((x2-x1)*(y4-y3) - (y2-y1)*(x4-x3))

      assert abs(t12_d) > EPS

      t12 = - t12_u / t12_d

      x12 = x1 + (x2-x1)*t12
      y12 = y1 + (y2-y1)*t12

      x34 = x3 + (x4-x3)*t34
      y34 = y3 + (y4-y3)*t34

      print(f't12 {t12} t34 {t34} ')
      assert abs(x12 - x34) < EPS and abs(y12 - y34) < EPS

      return MkPoint(x12,y12)

    # check only the line elongation would be intersected with circle
    # TODO : write test code
    @dispatch
    def is_inter(self, c:'MkCircle') -> bool: 
        x1 = self.p1.x
        y1 = self.p1.y
        xc = c.cen.x
        yc = c.cen.y

        l = self.l
        m = self.m 

        lc = x1 - xc
        mc = y1 - yc

        r = c.rad

        a = (l*l + m*m)
        b = 2*(l*lc + m*mc)
        c = lc*lc + mc*mc - r*r

        if b*b - 4*a*c < 0:
            print( f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}')
            return False
        else:
            return True

    # cut the circle c with self line
    # find the intersections between self line and circle c
    # TODO : write test code
    @dispatch
    def get_inter(self, c:'MkCircle'):# -> tuple(MkPoint, MkPoint):
        x1 = self.p1.x
        y1 = self.p1.y
        xc = c.cen.x
        yc = c.cen.y

        l = self.l
        m = self.m 

        lc = x1 - xc
        mc = y1 - yc

        r = c.rad

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

        pnt1 = self.get_p(t1) if 0 <= t1 and t1 <= 1 else None
        pnt2 = self.get_p(t2) if 0 <= t2 and t2 <= 1 else None

        return (pnt1, pnt2)


    # TODO : write test code
    @dispatch
    def is_inter(self, arc:'MkArc') -> bool: 
        x1 = self.p1.x
        y1 = self.p1.y
        xc = arc.cen.x
        yc = arc.cen.y

        l = self.l
        m = self.m 

        lc = x1 - xc
        mc = y1 - yc

        r = arc.rad

        a = (l*l + m*m)
        b = 2*(l*lc + m*mc)
        c = lc*lc + mc*mc - r*r

        if b*b - 4*a*c < 0:
            print( f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}')
            return False

        t1 = (-b+math.sqrt(b*b-4*a*c))/2/a
        t2 = (-b-math.sqrt(b*b-4*a*c))/2/a

        pnt1 = self.get_p(t1)
        pnt2 = self.get_p(t2)

        assert type(arc.whang(pnt1)) != bool and type(arc.whang(pnt2)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = arc.whang(pnt1)
        ang2 = arc.whang(pnt2)

        # either of two points is within the arc, then return true as it is intersected with line elongation anyway
        if arc.sang < ang1 and ang1 < arc.eang:
            return True

        if arc.sang < ang2 and ang2 < arc.eang:
            return True

        # if none of two points is within the arc, then return false as it is not intersected
        return False


    # TODO : write test code
    @dispatch
    def get_inter(self, arc:'MkArc'):

        if self.is_inter(arc) is False:
          return False

        x1 = self.p1.x
        y1 = self.p1.y
        xc = arc.cen.x
        yc = arc.cen.y

        l = self.l
        m = self.m 

        lc = x1 - xc
        mc = y1 - yc

        r = arc.rad

        a = (l*l + m*m)
        b = 2*(l*lc + m*mc)
        c = lc*lc + mc*mc - r*r
        
        if b*b - 4*a*c < 0:
            print( f'a: {a},b: {b},c: {c}, b*b - 4*a*c: {b*b - 4*a*c}')
            return False

        t1 = (-b+math.sqrt(b*b-4*a*c))/2/a
        t2 = (-b-math.sqrt(b*b-4*a*c))/2/a

        pnt1 = self.get_p(t1)
        pnt2 = self.get_p(t2)

        assert type(arc.whang(pnt1)) != bool and type(arc.whang(pnt2)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = arc.whang(pnt1)
        ang2 = arc.whang(pnt2)
        
        print(f'mkline::get_inter with arc pnt1 {pnt1} pnt2 {pnt2} t1 {t1} t2 {t2} ang1 {ang1} ang2 {ang2}')

        flag1 = flag2 = False

        # TODO: bug prone code, need thorough check, this does not work well...0 == 360 problem
        # either of two points is within the arc, then return true as it is intersected with line anyway
        if (arc.sang < ang1 and ang1 < arc.eang) or \
           (arc.sang+360 < ang1 and ang1 < arc.eang+360) or \
           (arc.sang-360 < ang1 and ang1 < arc.eang-360):
            flag1 = True

        if (arc.sang < ang2 and ang2 < arc.eang) or \
           (arc.sang+360 < ang2 and ang2 < arc.eang+360) or \
           (arc.sang-360 < ang2 and ang2 < arc.eang-360):
            flag2 = True

        if flag1 == False and flag2 == False:
            return False

        p1 = pnt1 if 0 <= t1 and t1 <= 1 and flag1 else None
        p2 = pnt2 if 0 <= t2 and t2 <= 1 and flag2 else None

        return (p1, p2)

    # returns true only if the projection point is in the line segment, 
    # otherwise returns false                                         |     
    #                                                              --------
    def is_in_proj(self, p:MkPoint) -> bool:
      x1 = self._p1.x
      y1 = self._p1.y
      x3 = p.x
      y3 = p.y

      l = self.l
      m = self.m

      t = - ( l*(x1-x3) + m*(y1-y3) ) / (l*l+m*m)

      print(f'l: {l}, m: {m}, x1: {x1}, y1: {y1}, x3: {x3}, y3: {y3} t is {t}')

      flag = True if 0 <= t and t <= 1 else False 

      return flag

    # only when the point is in the projection range
    # otherwise return false
    # it is for the command "trim"
    def get_in_proj(self, p:MkPoint) -> MkPoint: # or bool
      flag = self.is_in_proj(p)

      if not flag:
        return flag

      x1 = self._p1.x
      y1 = self._p1.y
      x3 = p.x
      y3 = p.y

      l = self.l
      m = self.m

      t = - ( l*(x1-x3) + m*(y1-y3) ) / (l*l+m*m)
      pp = self.get_p(t)

      return pp

    # regardless of the point in or out of projection range  
    # it is to be used for the command "extend"
    @dispatch
    def get_proj(self, p:MkPoint) -> MkPoint:

      x1 = self._p1.x
      y1 = self._p1.y
      x3 = p.x
      y3 = p.y

      l = self.l
      m = self.m

      t = - ( l*(x1-x3) +m*(y1-y3) ) / (l*l+m*m)
      pp = self.get_p(t)

      return pp

    # find projection point from self line to line l, for the command 'extend'
    @dispatch
    def get_proj(self, l:'MkLine') -> MkPoint:
      x1 = self._p1.x
      y1 = self._p1.y
      x2 = self._p2.x
      y2 = self._p2.y

      A = l.A
      B = l.B 
      C = l.C
      
      t = -(A*x1+B*y1+C)/(A*(x2-x1)+B*(y2-y1))

      return MkPoint(x1+(x2-x1)*t,y1+(y2-y1)*t)

    # find projection point from self line to circle c, for the command 'extend'
    # TODO : write test code
    @dispatch
    def get_proj(self, c:'MkCircle'):
      
      # check if line elongation is not intersected, then return false
      if self.is_inter(c) is False:
        return False

      # get two points that line elongation is intersected, no matter how far it is 
      pnt1, pnt2 = self.get_inter(c)

      # if any of two points are not None, than it is intersected with line segments, 
      # so can not be extended
      if pnt1 is None or pnt2 is None:
        return False

      # if both two points are none, that means those are not in the line segment
      # but in the line elongation, so can be extended
      if pnt1 is None and pnt2 is None:

        x1 = self._p1.x
        y1 = self._p1.y
        x2 = self._p2.x
        y2 = self._p2.y

        xc = c.cen.x
        yc = c.cen.y
        r = c.rad

        assert abs(x2-x1) + abs(y2-y1) >  EPS, 'MkLine::get_proj(circle) Strange line is almost a point, should be captured earlier'

        a = (x2-x1)*2 + (y2-y1)**2
        b = 2*(x2-x1)*(x1-xc)+2*(y2-y1)*(y1-yc)
        c =  (x1-xc)**2 + (y1-yc)**2 - r**2

        assert b**2 - 4*a*c > 0, f'b**2 - 4*a*c is {b**2 - 4*a*c} which is less than zero, needs to be checked'
        t1 = (-b + math.sqrt(b**2 - 4*a*c))/2/a
        t2 = (-b - math.sqrt(b**2 - 4*a*c))/2/a

        t = t1 if abs(t1) < abs(t2) else t2

        xt = x1 + (x2-x1)*t
        yt = y1 + (y2-y1)*t

        return MkPoint(xt,yt)

    # TODO : write test code
    @dispatch
    def get_proj(self, arc:'MkArc'):
      print('MkArc::get_proj is called')    
      if self.is_inter(arc) is False:
        print('!!!!!!!!!')
        return False

      pnt1, pnt2 = self.get_inter(arc)

      # if any of two points are not None, than it is intersected with line segments, 
      # so can not be extended
      if pnt1 is not None or pnt2 is not None:
        print('@@@@@@@@@@@@@@')
        return False

      if pnt1 is None and pnt2 is None:

        x1 = self._p1.x
        y1 = self._p1.y
        x2 = self._p2.x
        y2 = self._p2.y

        xc = arc.cen.x
        yc = arc.cen.y
        r  = arc.rad

        assert abs(x2-x1) + abs(y2-y1) >  EPS, 'MkLine::get_proj(circle) Strange line is almost a point, should be captured earlier'

        a = (x2-x1)*2 + (y2-y1)**2
        b = 2*(x2-x1)*(x1-xc)+2*(y2-y1)*(y1-yc)
        c =  (x1-xc)**2 + (y1-yc)**2 - r**2

        assert b**2 - 4*a*c > 0, f'b**2 - 4*a*c is {b**2 - 4*a*c} which is less than zero'
        t1 = (-b + math.sqrt(b**2 - 4*a*c))/2/a
        t2 = (-b - math.sqrt(b**2 - 4*a*c))/2/a

        pnt1 = self.get_p(t1)
        pnt2 = self.get_p(t2)

        assert type(arc.whang(pnt1)) != bool and type(arc.whang(pnt2)) != bool, 'MkArc::is_inter angle check failed'
        
        # if self.whang(pnt1) == False and self.whang(pnt2) == False:
        #     return False

        ang1 = arc.whang(pnt1)
        ang2 = arc.whang(pnt2)
        
        print(f'  MkLine::get_inter with arc pnt1 {pnt1} pnt2 {pnt2} t1 {t1} t2 {t2} ang1 {ang1} ang2 {ang2}')

        flag1 = flag2 = False

        # TODO: bug prone code, need thorough check, this does not work well...0 == 360 problem
        # either of two points is within the arc, then return true as it is intersected with line anyway
        if (arc.sang < ang1 and ang1 < arc.eang) or \
           (arc.sang+360 < ang1 and ang1 < arc.eang+360) or \
           (arc.sang-360 < ang1 and ang1 < arc.eang-360):
            flag1 = True

        if (arc.sang < ang2 and ang2 < arc.eang) or \
           (arc.sang+360 < ang2 and ang2 < arc.eang+360) or \
           (arc.sang-360 < ang2 and ang2 < arc.eang-360):
            flag2 = True

        print(f'  MkLine::get_inter with arc flag1 {flag1} flag2 {flag2} ')

        if flag1 is True and flag2 is True:
          t = t1 if abs(t1) < abs(t2) else t2

          xt = x1 + (x2-x1)*t
          yt = y1 + (y2-y1)*t

          return MkPoint(xt, yt)

        elif flag1 is True and flag2 is False:
          xt = x1 + (x2-x1)*t1
          yt = y1 + (y2-y1)*t1

          return MkPoint(xt, yt)

        elif flag1 is False and flag2 is True:
          xt = x1 + (x2-x1)*t2
          yt = y1 + (y2-y1)*t2

          return MkPoint(xt, yt)

        else:
          print('^^^^^^^^^^')
          return False

    # if b = False, dist is valid only when the projection 
    # is within range, otherwise return False
    @dispatch
    def dist(self, p:MkPoint, b: bool=True) -> float: # or bool
      
      flag = self.is_in_proj(p)
      if b == False and flag == False:
        return flag

      A = self.A
      B = self.B
      C = self.C 
      x1 = p.x
      y1 = p.y

      d = (A*x1+B*y1+C)/math.sqrt(A*A+B*B)

      return d

    @dispatch
    def dist(self, l:'MkLine') -> float:
      if self.is_inter(l):
        return 0

      d1 = self.dist(l._p1)
      d2 = self.dist(l._p2)

    # TODO : write test code
    @dispatch
    def dist(self, c:'MkCircle') -> float:
        d = self.dist(c.cen)
        return abs(d - c.rad, 0)

    # TODO : write test code
    @dispatch
    def dist(self, a:'MkArc') -> float:
        if a.is_inter(self):
            return False

        pp = self.get_proj(a.cen)
        lp = MkLine(a.cen,pp)

        if a.get_inter(lp) is not False:
            pnt1, pnt2  = a.get_inter(lp)

        assert pnt1 is not None or pnt2 is not None, 'MkArc::dist wrt line, both points are None'

        d1 = self.dist(pnt1) if pnt1 is not None else None
        d2 = self.dist(pnt2) if pnt2 is not None else None
        d3 = self.dist(a.spnt())
        d4 = self.dist(a.epnt())

        dl = [d1,d2,d3,d4]
        
        mindis = min(d for d in dl if d is not None)

        return mindis
        
    def offset(self, dist: float, dir : mkDir) -> 'MkLine': # dir : true : right, false : left
        x1 = self._p1.x
        x2 = self._p2.x
        y1 = self._p1.y
        y2 = self._p2.y

        dist = abs(dist)

        Len = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
        t = dist / Len if dir is mkDir.mkRIGHT else - dist/Len
        
        ox1 = x1 + (y2-y1)*t
        oy1 = y1 - (x2-x1)*t
        ox2 = x2 + (y2-y1)*t
        oy2 = y2 - (x2-x1)*t

        p1 = MkPoint(ox1,oy1)
        p2 = MkPoint(ox2,oy2)
        
        offline = MkLine(p1,p2)
        return offline

    def get_dir(self, p:MkPoint) -> mkDir:
      x1 = self.p2.x - self.p1.x 
      y1 = self.p2.y - self.p1.y 
      x2 = p.x - self.p1.x 
      y2 = p.y - self.p1.y

      d = x1 * y2 - x2 * y1

      return mkDir.mkLEFT if d > 0 else mkDir.mkRIGHT       

    # TODO : write test code
    # cut the line l with self
    @dispatch
    def trim(self, l:'MkLine', dir:mkDir) -> 'MkLine':
      if self.get_inter(l) is False:
        return False

      ip = self.get_inter(l)

      p1 = l.p1
      p2 = l.p2

      if dir == self.get_dir(p1):
        l.p1 = ip
        
      if dir == self.get_dir(p2):
        l.p2 = ip

      return l

    # TODO : write test code
    # cut circle with self line
    @dispatch
    def trim(self, c: 'MkCircle', dir:mkDir) -> 'MkArc':
        
        from mkarc import MkArc
        
        pnt1, pnt2 = self.get_inter(c)

        ang1 = c.whang(pnt1)
        ang2 = c.whang(pnt2)

        a = MkArc()

        a.cen = c.cen
        a.rad = c.rad

        a1 = min(ang1,ang2)
        a2 = max(ang1,ang2)
        ang1 = a1
        ang2 = a2

        midang = (a1+a2)/2

        midpnt = c.get_pnt(midang)

        middir = self.get_dir(midpnt)

        if dir is middir:
            a.sang = ang2
            a.eang = ang1+360
        else:
            a.sang = ang1
            a.eang = ang2
        
        return a

  # TODO : write test code
    # cut arc with self line
    @dispatch
    def trim(self, a: 'MkArc', dir:mkDir) -> 'MkArc':
        
        from mkarc import MkArc
        
        pnt1, pnt2 = self.get_inter(a)

        ang1 = a.whang(pnt1)
        ang2 = a.whang(pnt2)

        a.cen = a.cen
        a.rad = a.rad

        a1 = min(ang1,ang2)
        a2 = max(ang1,ang2)
        ang1 = a1
        ang2 = a2

        midang = (a1+a2)/2

        midpnt = a.get_pnt(midang)

        middir = self.get_dir(midpnt)

        if dir is middir:
            a.sang = ang2
            a.eang = ang1+360
        else:
            a.sang = ang1
            a.eang = ang2
        
        return a

    # TODO : write test code
    # elongate the self to the line l
    @dispatch
    def extend(self, l:'MkLine') -> 'MkLine':
      if self.get_inter(l) is True:
        return False

      ep = self.get_proj(l)

      d1 = self.p1.dist(ep)
      d2 = self.p2.dist(ep)

      if d1 > d2: # change p2 to ep
        self.p2 = ep
      else:
        self.p1 = ep

      return self

    # TODO : write test code, refactor needed to minimize the DRY
    @dispatch
    def extend(self, c: 'MkCircle'):

      print(f'MkLine::extend() with circle')

      if self.get_proj(c) is False:
        return False

      pnt = self.get_proj(c)
      t = self.get_t(pnt)

      if 0 <= t and t <= 1:
        return False

      if t > 1:
        self.p2 = pnt

      if t < 0:
        self.p1 = pnt

      print(f'MkLine::extend() with circle, t is {t}')

      self.calc_lm()
      self.Len = self.p1.dist(self.p2)

      return self

    # TODO : write test code, refactor needed to minimize the DRY
    @dispatch
    def extend(self, a: 'MkArc') -> 'MkLine': 
      print(f'MkLine::extend() with arc')

      if self.get_proj(a) is False:
        return False

      pnt = self.get_proj(a)
      t = self.get_t(pnt)

      if 0 <= t and t <= 1:
        return False

      if t > 1:
        self.p2 = pnt

      if t < 0:
        self.p1 = pnt

      print(f'MkLine::extend() with arc, t is {t}')

      self.calc_lm()
      self.Len = self.p1.dist(self.p2)

      return self
      
    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, _p1:MkPoint):
        self._p1 = _p1
        self.calc_lm()
        self.Len = self.p1.dist(self.p2)

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, _p2:MkPoint):
        self._p2 = _p2
        self.calc_lm()
        self.Len = self.p1.dist(self.p2)

    def conv(self, wtc: WorldToCanvas ): #
        qp1 = self._p1.conv(wtc)
        qp2 = self._p2.conv(wtc)
        self._qline = QLine(qp1,qp2)
        self.isconv = True

    def draw(self, qp):
        qp.drawLine(self._qline)

    def __repr__(self):
        return f"MkLine({self.p1}, {self.p2}, isconv {self.isconv})"
