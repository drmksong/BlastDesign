import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
import math
import unittest as ut

def OnPyInitApp():
    print("\nOnPyRx Lib")
    print("\ncommand = libtst")
    # manager.addPointMonitor(pm)    

def OnPyUnloadApp():
    print("\nOnPyUnloadApp")
    # manager.removePointMonitor(pm)

def OnPyLoadDwg():
    print("\nOnPyLoadDwg")

def OnPyUnloadDwg():
    print("\nOnPyUnloadDwg")

class MkCircle():
    def __init__(self,cen=Ge.Point3d(0, 0, 0),norm=Ge.Vector3d(0, 0, 1),ref=Ge.Vector3d(1, 0, 0),rad=1000,start=0,end=2*3.141592):
        self.Center = cen
        self.Norm = norm
        self.Ref = ref
        self.Radius = rad
        self.StartAngle = start
        self.EndAngle = end
        self.Circle = Db.Arc()
    
    def setRadius(self, r):
        self.Radius = r
        
    def setCenter(self, c):
        self.Center = c
        
    def setStartAngle(self, a):
        self.StartAngle = a

    def setEndAngle(self, a):
        self.EndAngle = a

    def setNorm(self, n):
        self.Norm = n

    def setRef(self, r):    
        self.Ref = r                

    def convDb(self)->Db.Arc:
        self.Circle = Db.Arc(self.Center,self.Norm,self.Radius,self.StartAngle,self.EndAngle)
        return self.Circle
    
    def measure(self,space):
        N = self.Radius*(self.EndAngle-self.StartAngle)/space
        theta = space/self.Radius
        print(f'N = {N}, theta = {theta}')

        return [
            (self.Radius*math.cos(self.StartAngle+theta*float(i))+self.Center[0],
             self.Radius*math.sin(self.StartAngle+theta*float(i))+self.Center[1]) 
            for i in range(round(N))
        ]

    def appendDb(self,model):
        # self.convDb()
        self.Circle = Db.Arc(self.Center,self.Norm,self.Radius,self.StartAngle,self.EndAngle)
        model.appendAcDbEntity(self.Circle)


class MkLine():
    def __init__(self,start=Ge.Point3d(0, 0, 0),end=Ge.Point3d(0, 0, 0)):
        self.Start = start
        self.End = end
        self.Length = self.Start.distanceTo(self.End)
        self.Line = Db.Line()

    def setStart(self, s):
        self.Start = s

    def setEnd(self, e):    
        self.End = e

    def convDb(self)->Db.Line:
        self.Line = Db.Line(self.Start,self.End)
        return self.Line
    
    def measure(self,space):
        N = (self.Length/space)
        s = self.Start
        e = self.End
        return [
            ((e[0]-s[0])*float(i)/N+s[0],
             (e[1]-s[1])*float(i)/N+s[1]) 
            for i in range(round(N))
        ]
    
    def scale(self,sc):
        m = [(self.Start[0]+self.End[0])/2,(self.Start[1]+self.End[1])/2]
        s = self.Start
        e = self.End

        self.Start = Ge.Point3d(m[0]+sc*(s[0]-m[0]),m[1]+sc*(s[1]-m[1]),0)
        self.End   = Ge.Point3d(m[0]+sc*(e[0]-m[0]),m[1]+sc*(e[1]-m[1]),0)
    
    # edge is the length of the edge to be trimmed
    def trimEdge(self,edge):
        s = self.Start
        e = self.End
        m = Ge.Point3d((s[0]+e[0])/2,(s[1]+e[1])/2,0)

        if self.Length < 2*edge:
            self.Start = m
            self.End = m

        else:
            self.Start = Ge.Point3d(m[0]+(s[0]-m[0])*(self.Length-2*edge)/self.Length,m[1]+(s[1]-m[1])*(self.Length-2*edge)/self.Length,0)
            self.End   = Ge.Point3d(m[0]+(e[0]-m[0])*(self.Length-2*edge)/self.Length,m[1]+(e[1]-m[1])*(self.Length-2*edge)/self.Length,0)

    # dir = 1 if offset is to the right, -1 if offset is to the left, otherwise no offset
    def offset(self,off,dir):
        if dir == 1:
            s = self.Start
            e = self.End
        elif dir == -1:
            s = self.End
            e = self.Start
        else:
            return

        m = Ge.Point3d((s[0]+e[0])/2,(s[1]+e[1])/2,0)

        vec = Ge.Vector3d(e[0]-s[0],e[1]-s[1],0).normalize()
        vert = Ge.Vector3d(0,0,1)
        nrm = vec.crossProduct(vert)

        nm = Ge.Point3d(m[0]+nrm[0]*off,m[1]+nrm[1]*off,0)

        ns = Ge.Point3d(nm[0]+(s[0]-m[0]),nm[1]+(s[1]-m[1]),0)
        ne = Ge.Point3d(nm[0]+(e[0]-m[0]),nm[1]+(e[1]-m[1]),0)
        return MkLine(ns,ne)

    def appendDb(self,model):
        self.convDb()
        model.appendAcDbEntity(self.Line)


class MkPolyLine():
    def __init__(self,pts=[]):
        self.Points = pts
        self.Poly = Db.Polyline()
    
    def addPoint(self,p):
        self.Points.append(p)

    def addArc(self,a):
        pass

    def convDb(self)->Db.Polyline:
        self.Poly = Db.Polyline()
        for p in self.Points:
            self.Poly.addVertexAt(len(self.Points),p,0,0,0)
        return self.Poly
    
    def appendDb(self,model):
        self.convDb()
        model.appendAcDbEntity(self.Poly)


class MkTunnel():
    def __init__(self):
        self.Center = Ge.Point3d(-100000, -100000, 0)
        self.Radius = 10000
        self.StartAngle = 0
        self.EndAngle = 2 * 3.14159

        self.Circles = []
        self.Lines = []
        self.Polyline = Db.Polyline()

    def buildPoly(self,elist):
        self.Polyline = Db.Polyline(elist)
        return self.Polyline

    def appendDb(self,model):
        for c in self.Circles:
            print(c)
            c.appendDb(model)
        for l in self.Lines:
            print(l)
            l.appendDb(model)


def PyRxCmd_libtst():
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
        len = 100
        cen = [Ge.Point3d(x,y,0) for x in range(0,100,10) for y in range(0,100,10)]
        norm = Ge.Vector3d(0, 0, 1)
        ref = Ge.Vector3d(1, 0, 0)
        rad = 1
        ang = [[s,e] for s in range(0,180,45) for e in range(180,360,45)]
        
        l1mk = MkLine(Ge.Point3d(-len/2, -30 ,0), Ge.Point3d(len/2,30,0))
        l2mk = MkLine(Ge.Point3d(-len/2, -50 ,0), Ge.Point3d(len/2,10,0))
        l3mk = MkLine(Ge.Point3d(-len/2, -70 ,0), Ge.Point3d(len/2,-10,0))
        l2mk.scale(1.5)
        l3mk.scale(2)
        l3mk.trimEdge(10)
        l4mk = l3mk.offset(10,1)

        l1mk.appendDb(model)
        l2mk.appendDb(model)
        l3mk.appendDb(model)
        l4mk.appendDb(model)

        mes = l2mk.measure(7.0)
        for m in mes:
            rx,ry = m
            print(rx,ry)
        cen = [Ge.Point3d(rx,ry,0) for rx,ry in mes]
        print(cen)
        # cirs = [MkCircle(Ge.Point3d(res[i][0],res[i][1],0),norm,ref,rad,0,359) for i in range(len(res))]
        cirs = [MkCircle(c,norm,ref,rad) for c in cen]

        # print(cirs)
        for c in cirs:
            c.appendDb(model)

        # rad = 100
        # cen = Ge.Point3d(0,-200,0)
        # tun1 = MkCircle(cen,norm,ref,rad,-30*3.14159/180,90*3.14159/180)
        # tun2 = MkCircle(cen,norm,ref,rad,90*3.14159/180,210*3.14159/180)
        # tun1.appendDb(model)
        # tun2.appendDb(model)

        # tun2.setRadius(90)

        MkPolyLine([Ge.Point3d(0,0,0),Ge.Point3d(100,0,0),Ge.Point3d(100,100,0),Ge.Point3d(0,100,0),Ge.Point3d(0,0,0)]).appendDb(model)
        MkTunnel().appendDb(model)

        # mes = tun2.measure(10.0)
        # print(mes)
        # rad = 1

        # for m in mes:
        #     mx,my = m
        #     print(f'mx={mx},yr={my}')
        # cen = [Ge.Point3d(mx,my,0) for mx,my in mes]
        # cen2 = [Ge.Point3d(-mx,my,0) for mx,my in mes[1:]]

        # cirs = [MkCircle(c,norm,ref,rad) for c in cen]
        # cirs2 = [MkCircle(c,norm,ref,rad) for c in cen2]

        # for c in cirs:
        #     c.appendDb(model)
        # for c in cirs2:
        #     c.appendDb(model)


    except Exception as err:
        print(err)


