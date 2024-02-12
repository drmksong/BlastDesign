import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
# from inputMonitor import *
import math

def OnPyInitApp():
    print("\nOnPyInitApp")
    print("\ncommand = pydoit")
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
    
    def appendDb(self,model):
        # self.convDb()
        self.Circle = Db.Arc(self.Center,self.Norm,self.Radius,self.StartAngle,self.EndAngle)
        model.appendAcDbEntity(self.Circle)


class MkLine():
    def __init__(self,start=Ge.Point3d(0, 0, 0),end=Ge.Point3d(0, 0, 0)):
        self.Start = start
        self.End = end
        self.Line = Db.Line()

    def setStart(self, s):
        self.Start = s

    def setEnd(self, e):    
        self.End = e

    def convDb(self)->Db.Line:
        self.Line = Db.Line(self.Start,self.End)
        return self.Line
    
    def appendDb(self,model):
        self.convDb()
        model.appendAcDbEntity(self.Line)
        

class Tunnel():
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


# manager = Ap.curDoc().inputPointManager()
# t = Tunnel()
def PyRxCmd_doit():
    try:
        # get the working database, database is also a property of Document
        db = Db.HostApplicationServices().workingDatabase()

        # create a Polyline
        pline = Db.Polyline(2)
        pline.setDatabaseDefaults()
        
        #zero based
        pline.addVertexAt(0, Ge.Point2d(-1732.0508, -1000),0.09535,0,0)
        pline.addVertexAt(1, Ge.Point2d(1732.0508, -1000),0.372852577,0,0)
        # pline.addVertexAt(3, Ge.Point2d(-800, -600))
        pline.setClosed(True)


        # set a color
        color = Db.Color()
        color.setRGB(255, 0, 255)
        pline.setColor(color)

        # open modelspace for write and add the entity
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
        model.appendAcDbEntity(pline)

        # python garbage collects here, circle and model will be closed or deleted
        # here

    except Exception as err:
        print(err)    

def PyRxCmd_pydoit():    
    try:
        t = Tunnel()        
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
        cen = Ge.Point3d(0, 0, 0)
        cen2 = Ge.Point3d(-129.9038, -75, 0)
        cen3 = Ge.Point3d( 129.9038, -75, 0)
        cen4 = Ge.Point3d( 0, 51147.1911, 0)
        norm = Ge.Vector3d(0, 0, 1)
        ref = Ge.Vector3d(1, 0, 0)
        rad = 5700.0000
        rad2 = 5850.0000
        rad4 = 53897.1911
        len = 11431.5353

        l1 = Ge.Line3d(Ge.Point3d(-1000, -1000,0), Ge.Point3d(1000,  1000,0))
        l2 = Ge.Line3d(Ge.Point3d(-1000,  1000,0), Ge.Point3d(1000, -1000,0))
        pl1 = Ge.Plane(Ge.Point3d(0, -100, 0), Ge.Vector3d(0,1,0))

        sang1 =  30.0/180*3.14159
        eang1 = 150.0/180*3.14159

        c1 = Ge.CircArc3d(cen, norm, ref, rad,sang1,eang1)
        
        sang2 = -24.4804/180*3.14159
        eang2 =  30.0000/180*3.14159
        
        c2 = Ge.CircArc3d(cen2, norm, ref, rad2, sang2, eang2)
        
        sang3 = 150.0000/180*3.14159
        eang3 = 204.4804/180*3.14159

        c3 = Ge.CircArc3d(cen3, norm, ref, rad2, sang3, eang3)

        sang4 = 264.4697/180*3.14159
        eang4 = 275.5303/180*3.14159

        pc = c1.intersectWith(pl1)
        print(pc)
        print(pc[2])
        print(pc[3])

        sang = math.atan2(pc[2].y-cen.y, pc[2].x-cen.x)
        eang = math.atan2(pc[3].y-cen.y, pc[3].x-cen.x)

        sang =  30.0/180*3.14159
        eang = 120.0/180*3.14159
    
        # sang = 0.0
        # eang = 3.14159/2
        # center, normal, radius, start angle, end angle
        a1 = Ge.CircArc3d (cen, norm, ref, rad, sang, eang)
        pl =l1.intersectWith(l2)        

        # trim l1 by l2 from start point of l1 to the intersection point
        # l1db = Db.Line(l1.getStartPoint(), l1.getEndPoint())
        # l2db = Db.Line(l2.getStartPoint(), l2.getEndPoint())

        # l1db = Db.Line(pl[1], Ge.Point3d(1000,  1000,0))
        # l2db = Db.Line(Ge.Point3d(-1000,  1000,0), Ge.Point3d(1000, -1000,0))
        # ben =  Db.Line(Ge.Point3d(-len/2, -300 ,0), Ge.Point3d(len/2,-300,0))
        # a1db = Db.Arc(cen , norm, rad , sang1, eang1)
        # a2db = Db.Arc(cen2, norm, rad2, sang2, eang2)
        # a3db = Db.Arc(cen3, norm, rad2, sang3, eang3)
        # a4db = Db.Arc(cen4, norm, rad4, sang4, eang4)

        # print(pl)
        
        # model.appendAcDbEntity(l1db)
        # model.appendAcDbEntity(l2db)
        # model.appendAcDbEntity(a1db)
        # model.appendAcDbEntity(a2db)
        # model.appendAcDbEntity(a3db)
        # model.appendAcDbEntity(a4db)
        # model.appendAcDbEntity(ben)

        a1mk = MkCircle(cen ,norm,ref,rad,sang1,eang1)
        a2mk = MkCircle(cen2,norm,ref,rad2,sang2,eang2)
        s3mk = MkCircle(cen3,norm,ref,rad2,sang3,eang3)
        a4mk = MkCircle(cen4,norm,ref,rad4,sang4,eang4)
        l1mk = MkLine(Ge.Point3d(-len/2, -300 ,0), Ge.Point3d(len/2,-300,0))
        
        # a1mk.appendDb(model)
        # a2mk.appendDb(model)
        # s3mk.appendDb(model)
        # a4mk.appendDb(model)
        # l1mk.appendDb(model)

        t.Circles.append(a1mk)
        t.Circles.append(a2mk)
        t.Circles.append(s3mk)
        t.Circles.append(a4mk)
        t.Lines.append(l1mk)

        t.appendDb(model)

        l3db = Db.Line(Ge.Point3d(-1000,  1000,0), Ge.Point3d(0,0,0))
        l4db = Db.Line(Ge.Point3d(0,0,0), Ge.Point3d(1000,  1000,0))

        pline = Db.Polyline()
        pline.addVertexAt(0, Ge.Point2d(-1000,  1000))
        pline.addVertexAt(1, Ge.Point2d(0,0))
        pline.addVertexAt(2, Ge.Point2d(1000,  1000))
        a1mk.Circle.toPolyline(pline)
        
        model.appendAcDbEntity(pline)

    except Exception as err:
        print(err)

# def PyRxCmd_test():    
#     try:
#         db = Db.HostApplicationServices().workingDatabase()
#         model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
#         doc = Ap.curDoc()
#         pnt = Ed.Editor.getPoint("Pick a point for the center of the circle:")
#         print(pnt[0], pnt[1])
        
#         t.Center = pnt[1]
#         # t.Radius = 1000
#         t.Circle.setCenter(t.Center)
#         t.Circle.setRadius(t.Radius)

#         c = model.appendAcDbEntity(t.Circle)
#         c.radius = t.Radius-1000
#         print(c)
        
#         doc.updateScreen()
#     except Exception as err:
#         print(err)

# def PyRxCmd_doit():
#     try:
#         db = Db.HostApplicationServices().workingDatabase()
#         model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
#         doc = Ap.curDoc()
#         pnt1 = Ed.Editor.getPoint("Pick a point for the point 1 of the line:")
        
#         pnt2 = Ed.Editor.getPoint("Pick a point for the point 2 of the line:")
        
#         t.Center = pnt1[1]
#         t.Line = Db.Line(pnt1[1], pnt2[1])
#         # t.Radius = 1000
#         t.Circle.setCenter(t.Center)
#         t.Circle.setRadius(t.Radius)
#         c = model.appendAcDbEntity(t.Circle)
#         l = model.appendAcDbEntity(t.Line)
#         c.radius = t.Radius-1000
#         c.update()
#         doc.updateScreen()
#     except Exception as err:
#         print(err)