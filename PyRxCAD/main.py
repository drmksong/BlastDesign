import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
# from inputMonitor import *
import math
from lib import MkCircle, MkLine, MkTunnel, MkPolyLine

def OnPyInitApp():
    print("\nOnPyInitApp")
    print("\ncommand = main")
    # manager.addPointMonitor(pm)    

def OnPyUnloadApp():
    print("\nOnPyUnloadApp")
    # manager.removePointMonitor(pm)

def OnPyLoadDwg():
    print("\nOnPyLoadDwg")

def OnPyUnloadDwg():
    print("\nOnPyUnloadDwg")





# manager = Ap.curDoc().inputPointManager()
# t = Tunnel()
            
# tun is to be used as a command in AutoCAD
# to draw a tunnel profile
#
def PyRxCmd_main():
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


    
def PyRxCmd_tu():
    try:
        # get the working database, database is also a property of Document
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)

        mkpl = MkPolyLine()
        mktun = MkTunnel()  

        # create a Polyline
        pline = Db.Polyline()

        pnts = [
            (5194.2024 ,    0.0000),
            (4936.3448 , 5349.1272),
            (-4936.3448, 5349.1272),
            (-5194.2024,    0.0000),
        ]  

        gepnts = [Ge.Point2d(x,y) for x,y in pnts]

        cen = [(-129.9038,2424.1272 ),
            (   0.0000,2499.1272 ),
            ( 129.9038,2424.1272 ),
            (   0.0000,53646.3183)
        ]

        rad = [5850.0000,
            5700.0000,
            5850.0000,
            53897.1911
        ]

        cirs = [MkCircle(Ge.Point3d(c[0],c[1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),r,0,3.14159*2) for c,r in zip(cen,rad)]
        for c in cirs:          
            c.appendDb(model)

        ang = []
        for i, c in enumerate(cen):
            s = pnts[i]
            e = pnts[(i+1)%4]
            v1 = Ge.Vector2d(s[0]-c[0],s[1]-c[1])
            v2 = Ge.Vector2d(s[0]-e[0],s[1]-e[1])
            ang.append(v1.angleTo(v2))
        print(ang)

        # verge is necessary to present arc of the tunnel profile 
        verge = [math.tan(math.pi/2+a) if a > math.pi/2 else math.tan((math.pi/2-a)/2) for a in ang]
        print(verge)

        pline.setDatabaseDefaults()
        pline.addVertexAt(0,gepnts[0], verge[0], 0, 0)
        pline.addVertexAt(1,gepnts[1], verge[1], 0, 0)
        pline.addVertexAt(2,gepnts[2], verge[2], 0, 0)
        pline.addVertexAt(3,gepnts[3], verge[3], 0, 0)
        pline.setClosed(True)

        #zero based
        # pline.addVertexAt(0, Ge.Point2d(-1732.0508, -1000),0.09535,0,0)
        # pline.addVertexAt(1, Ge.Point2d(1732.0508, -1000),0.372852577,0,0)
        # # pline.addVertexAt(3, Ge.Point2d(-800, -600))
        # pline.setClosed(True)

        # set a color
        color = Db.Color()
        color.setRGB(255, 0, 255)
        pline.setColor(color)

        # open modelspace for write and add the entity

        model.appendAcDbEntity(pline)

        # python garbage collects here, circle and model will be closed or deleted
        # here    
    except Exception as err:
        print(err)

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
        t = MkTunnel()        
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

def PyRxCmd_doit2():
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