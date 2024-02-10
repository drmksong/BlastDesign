import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
from inputMonitor import *


class Tunnel():
    def __init__(self):
        self.Center = Ge.Point3d(-100000, -100000, 0)
        self.Radius = 10000
        self.StartAngle = 0
        self.EndAngle = 2 * 3.14159

        self.Circle = Db.Circle()
        self.Line = Db.Line()


def OnPyInitApp():
    print("\nOnPyInitApp")
    print("\ncommand = pydoit")
    manager.addPointMonitor(pm)    

def OnPyUnloadApp():
    print("\nOnPyUnloadApp")
    manager.removePointMonitor(pm)

def OnPyLoadDwg():
    print("\nOnPyLoadDwg")

def OnPyUnloadDwg():
    print("\nOnPyUnloadDwg")


manager = Ap.curDoc().inputPointManager()
t = Tunnel()

def PyRxCmd_pydoit():    
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)

        l1 = Ge.Line3d(Ge.Point3d(-1000, -1000,0), Ge.Point3d(1000,  1000,0))
        l2 = Ge.Line3d(Ge.Point3d(-1000,  1000,0), Ge.Point3d(1000, -1000,0))
        p=l1.intersectWith(l2)        
        # trim l1 by l2 from start point of l1 to the intersection point
        # l1db = Db.Line(l1.getStartPoint(), l1.getEndPoint())
        # l2db = Db.Line(l2.getStartPoint(), l2.getEndPoint())
        l1db = Db.Line(p[1], Ge.Point3d(1000,  1000,0))
        l2db = Db.Line(Ge.Point3d(-1000,  1000,0), Ge.Point3d(1000, -1000,0))

        print(p)
        
        model.appendAcDbEntity(l1db)
        model.appendAcDbEntity(l2db)
        

    except Exception as err:
        print(err)

def PyRxCmd_test():    
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
        doc = Ap.curDoc()
        pnt = Ed.Editor.getPoint("Pick a point for the center of the circle:")
        print(pnt[0], pnt[1])
        
        t.Center = pnt[1]
        # t.Radius = 1000
        t.Circle.setCenter(t.Center)
        t.Circle.setRadius(t.Radius)

        c = model.appendAcDbEntity(t.Circle)
        c.radius = t.Radius-1000
        print(c)
        
        doc.updateScreen()
    except Exception as err:
        print(err)

def PyRxCmd_doit():
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)
        doc = Ap.curDoc()
        pnt1 = Ed.Editor.getPoint("Pick a point for the point 1 of the line:")
        
        pnt2 = Ed.Editor.getPoint("Pick a point for the point 2 of the line:")
        
        t.Center = pnt1[1]
        t.Line = Db.Line(pnt1[1], pnt2[1])
        # t.Radius = 1000
        t.Circle.setCenter(t.Center)
        t.Circle.setRadius(t.Radius)
        c = model.appendAcDbEntity(t.Circle)
        l = model.appendAcDbEntity(t.Line)
        c.radius = t.Radius-1000
        c.update()
        doc.updateScreen()
    except Exception as err:
        print(err)