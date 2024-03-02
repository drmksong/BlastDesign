
import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed

from lib import *
from mkblast import *
from enum import Enum

class MkTunnelProfile(MkPolyLine): 
    def __init__(self):
        super().__init__()
        self.Center = Ge.Point3d(0, 0, 0)

    def setCenter(self, c:Ge.Point3d): # TODO: delete it if it is not necessary
        self.Center = c

    def buildTunnel(self):
        try:
            # get the working database, database is also a property of Document
            db = Db.HostApplicationServices().workingDatabase()
            model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)

            mkpl = MkPolyLine()

            # create a Polyline
            self.Polyline = Db.Polyline()

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

            cirs = [MkArc(Ge.Point3d(c[0],c[1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),r,0,3.14159*2) for c,r in zip(cen,rad)]
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

            self.Polyline.setDatabaseDefaults()
            self.Polyline.addVertexAt(0,gepnts[0], verge[0], 0, 0)
            self.Polyline.addVertexAt(1,gepnts[1], verge[1], 0, 0)
            self.Polyline.addVertexAt(2,gepnts[2], verge[2], 0, 0)
            self.Polyline.addVertexAt(3,gepnts[3], verge[3], 0, 0)
            self.Polyline.setClosed(True)

            #zero based
            # self.Polyline.addVertexAt(0, Ge.Point2d(-1732.0508, -1000),0.09535,0,0)
            # self.Polyline.addVertexAt(1, Ge.Point2d(1732.0508, -1000),0.372852577,0,0)
            # # self.Polyline.addVertexAt(3, Ge.Point2d(-800, -600))
            # self.Polyline.setClosed(True)

            # set a color
            color = Db.Color()
            color.setRGB(255, 0, 255)
            self.Polyline.setColor(color)

            # open modelspace for write and add the entity

            model.appendAcDbEntity(self.Polyline)

            # python garbage collects here, circle and model will be closed or deleted
            # here    
        except Exception as err:
            print(err)


class MkTunnel():
    def __init__(self):
        self.ReferencePoint = MkPoint
        self.Profile = MkTunnelProfile()
        self.ChargeCurve = [] # list of MkChargeCurve, which is the layout of blast lines and arcs
        self.BlastHoles = MkBlastHoles() # list of MkBlastHole
        self.CenterCutHoles = MkCenterCutHoles() # list of MkBlastHole
        self.ChargeDensity = 0.0 # charge density of the tunnel
        self.AdvaceLength = 0.0 # advance length of the tunnel
        self.DetonatorSummary = {}
        self.ExplosiveSummary = {}
        self.BlastHoleSummary = {}
        self.ExcavationSummary = {}

    def iniDetoSummary(self):
        self.DetonatorSummary = {
            "Starter":0,
            "MS":0,
            "LP":0,
            "Bunch":0,
        }

    def iniExploSummary(self):
        self.ExplosiveSummary = {
            "ANFOWeight": 0,
            "EmulsionWeight": 0,
            "DynamiteWeight": 0,
            "FinexWeight": 0,
            "TotalChargeWeight":0,
            "ANFOCartridgeNo":0,
            "EmulsionCartridgeNo":0,
            "DynamiteCartridgeNo":0,
            "FinexCartridgeNo":0,
            "TotalCartridgeNo":0,
        }

    def iniBlastHoleSummary(self):
        self.BlastHoleSummary = {
            "CutHoleNo" : [],
            "StoppingHoleNo" : [], # uppder and lower holes
            "FloorHoleNo" : 0,
            "SmoothBlastHoleNo" : 0,
            "TotalHoleNo" : 0,
            "CutHoleLength":0,
            "StoppingHoleLength":0,
            "FloorHoleLength":0,
            "SmoothBlastHoleLength":0,
            "TotalHoleLength":0,
        }

    def iniExcavationSummary(self):
        self.ExcavationSummary = {
            "Area":0.0,
            "DrillLength":0.0,
            "AdvanceLength":0.0,
            "TotalChargeWeight":0.0, # check redundancy
            "TotalCartrigeNo":0,
            "TotalExcavationVolume":0.0,
            "SpecificCharge":0.0,
            "SpecificCartrigeNo":0,
            "SpecificDrillLength":0.0
        }

    def determineCenterCutLoc(self,hint:str):
        if hint == "center": # place center cut holes at the center of the tunnel
            loc = []
            loc.append((0,2000))
            loc.append((0,0))

            return [(0,0)] # these locations are local coordinates, not global, which is self.ReferencePoint
        elif hint == "left": # place center cut holes at the left side of the tunnel
            return [(-100,0)]
        elif hint == "right": # place center cut holes at the right side of the tunnel
            return [(100,0)]
        else:
            return []

    def placeCenterCut(self,nhole:int, loc:list):
        def placeEmptyHole(nhole,loc):
            for i in range(nhole):
                bh = MkBlastHole(Ge.Point3d(loc[i][0],loc[i][1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),self.EmptyHoleRadius)
                bh.NumCartrige = [0]
                bh.BlastHoleType = enumBlastHoleType.EmptyHole
                bh.CutHoleType = enumCutHoleType.EmptyHole
                bh.ExplosiveTypes = [enumExplosiveType.NonExplosive]
                bh.ChargeWeights = [0.0]
                bh.DetonatorType = enumDetonatorType.NoneDetonator
                bh.ParentChargeCurve = None
                bh.TotalLength = 0.0
                bh.TampingLength = 0.0
                self.addBlastHole(bh)


        def placeFirstCut(nhole,loc):
            for i in range(nhole):
                bh = MkBlastHole(Ge.Point3d(loc[i][0],loc[i][1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),self.BlastHoleRadius)
                bh.NumCartrige = [0]
                bh.BlastHoleType = enumBlastHoleType.CenterCutHole
                bh.CutHoleType = enumCutHoleType.FirstCut
                bh.ExplosiveTypes = [enumExplosiveType.Emulsion]
                bh.ChargeWeights = [0.0]
                bh.DetonatorType = enumDetonatorType.NoneDetonator
                bh.ParentChargeCurve = None
                bh.TotalLength = 0.0
                bh.TampingLength = 0.0
                self.addBlastHole(bh)

        def placeSecondCut(nhole,loc):
            for i in range(nhole):
                bh = MkBlastHole(Ge.Point3d(loc[i][0],loc[i][1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),self.BlastHoleRadius)
                bh.BlastHoleType = enumBlastHoleType.CenterCutHole
                bh.CutHoleType = enumCutHoleType.SecondCut
                self.addBlastHole(bh)

        def placeThirdCut(nhole,loc):
            for i in range(nhole):
                bh = MkBlastHole(Ge.Point3d(loc[i][0],loc[i][1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),self.BlastHoleRadius)
                bh.BlastHoleType = enumBlastHoleType.CenterCutHole
                bh.CutHoleType = enumCutHoleType.ThirdCut
                self.addBlastHole(bh)

        def placeFourthCut(nhole,loc):
            for i in range(nhole):
                bh = MkBlastHole(Ge.Point3d(loc[i][0],loc[i][1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),self.BlastHoleRadius)
                bh.BlastHoleType = enumBlastHoleType.CenterCutHole
                bh.CutHoleType = enumCutHoleType.FourthCut
                self.addBlastHole(bh)

        placeEmptyHole(nhole,loc)
        placeFirstCut(nhole,loc)
        placeSecondCut(nhole,loc)
        placeThirdCut(nhole,loc)
        placeFourthCut(nhole,loc)

    def placeStoppingHole(self,nhole:int, loc:list):
        pass

    def placeFloorHole(self,nhole:int, loc:list):
        pass

    def placeSmoothBlastHole(self,nhole:int, loc:list):
        pass
        
    
    def addBlastHole(self,l:MkBlastHole):
        self.BlastHole.append(l)

    def addChargeCurve(self, a:MkChargeCurve):
        self.ChargeCurve.append(a)


    def appendDb(self,model:Db.BlockTableRecord,debug=False):
        for a in self.Arcs:
            if debug: print(a)
            a.appendDb(model)
        for l in self.Lines:
            if debug: print(l)
            l.appendDb(model)
        for bh in self.BlastHole:
            if debug: print(bh)
            bh.appendDb(model)


def PyRxCmd_tutst():
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)

        ##### line test #######
        # lines = MkTunnel()
        # lines.addLine(MkLine(Ge.Point3d(0, 0, 0), Ge.Point3d(1000, 0, 0)))
        # lines.addLine(MkLine(Ge.Point3d(1000, 0, 0), Ge.Point3d(1000, 1000, 0)))
        # lines.addLine(MkLine(Ge.Point3d(1000, 1000, 0), Ge.Point3d(0, 1000, 0)))
        # # lines.addLine(MkLine(Ge.Point3d(0, 1000, 0), Ge.Point3d(0, 0, 0)))
        # lines.buildPoly()

        tunnel = MkTunnel()
        tp = tunnel.Profile
        df = pd.read_csv('tp_c1.csv')
        # iloc[row, column]
        # column - 0:pnt_x, 1:pnt_y, 2:verge, 3:cen_x, 4:cen_y, 5:rad, 6:sang, 7:eang
        # print(df.iloc[0,0],df.iloc[0,1],df.iloc[0,2],df.iloc[0,3],df.iloc[0,4])
        for i in range(len(df)):
            # sum = 3*df['pnt_y'] 
            # print(f'sum = {sum}\n')
            ## cen=Ge.Point3d(0, 0, 0),norm=Ge.Vector3d(0, 0, 1),ref=Ge.Vector3d(1, 0, 0),rad=1000,start=0,end=2*3.141592
            cen_x,cen_y = df.iloc[i,3],df.iloc[i,4]
            cen = Ge.Point3d(df.iloc[i,3],df.iloc[i,4],0)
            norm = Ge.Vector3d(0, 0, 1)
            ref=Ge.Vector3d(1, 0, 0)
            rad = df.iloc[i,5]
            sang = df.iloc[i,6]*3.14159/180
            eang = df.iloc[i,7]*3.14159/180
            # print(f'cen = ({cen_x},{cen_y}), rad = {rad}, sang = {sang}, eang = {eang}')
            tp.addArc(MkArc(cen,norm,ref,rad,sang,eang))
        
        # print(df)
        tp.Color.setRGB(255,0,255)
        tp.buildPoly()
        tp.appendDb(model)

        # tunnel.addLine(MkLine(Ge.Point3d(-1000, 1000, 0), Ge.Point3d( 1000, 1000, 0)))
        # tunnel.addLine(MkLine(Ge.Point3d( 1000, 1000, 0), Ge.Point3d( 1000, 3000, 0)))
        # tunnel.addLine(MkLine(Ge.Point3d( 1000, 3000, 0), Ge.Point3d(-1000, 3000, 0)))
        # tunnel.addLine(MkLine(Ge.Point3d(-1000, 3000, 0), Ge.Point3d(-1000, 1000, 0)))

        lines = []
        lines.append([-1000,1000,1000,1000])
        lines.append([ 1000,1000,1000,3000])
        lines.append([ 1000,3000,-1000,3000])
        lines.append([-1000,3000,-1000,1000])

        for i in range(1,4):
            lines.append([-1000-i*900,1000,-1000-i*900,3000])
            lines.append([ 1000+i*900,1000, 1000+i*900,3000])

        for i in range(1,5) :  
            y = 3000+i*800
            x = math.sqrt((5500-800)**2-(y-2550)**2) - 850 
            lines.append([-x,3000+i*800, x,3000+i*800])
            

        for l in lines:
            line = MkLine(Ge.Point3d(l[0],l[1],0), Ge.Point3d(l[2],l[3],0))
            tunnel.addLine(line)
            pnts = line.measure(600)
            for p in pnts:
                bh = MkCircle(Ge.Point3d(p[0],p[1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),50)
                bh.Color.setRGB(0,255,0)
                tunnel.addBlasthole(bh)

        arcs = []

        for i in range(len(df)):
            cen_x,cen_y = df.iloc[i,3],df.iloc[i,4]
            cen = Ge.Point3d(df.iloc[i,3],df.iloc[i,4],0)
            norm = Ge.Vector3d(0, 0, 1)
            ref=Ge.Vector3d(1, 0, 0)
            rad = df.iloc[i,5]-50
            sang = df.iloc[i,6]*3.14159/180
            eang = df.iloc[i,7]*3.14159/180
            arcs.append([cen,norm,ref,rad,sang,eang])

        for i in range(len(df)-1):
            cen_x,cen_y = df.iloc[i,3],df.iloc[i,4]
            cen = Ge.Point3d(df.iloc[i,3],df.iloc[i,4],0)
            norm = Ge.Vector3d(0, 0, 1)
            ref=Ge.Vector3d(1, 0, 0)
            rad = df.iloc[i,5]-850
            sang = df.iloc[i,6]*3.14159/180
            eang = df.iloc[i,7]*3.14159/180
            arcs.append([cen,norm,ref,rad,sang,eang])

        for i,a in enumerate(arcs):
            print(f'i {i}')
            cen,norm,ref,rad,sang,eang = a
            arc = MkArc(cen,norm,ref,rad,sang,eang)
            arc.Color.setRGB(255,255,0)
            pnts = arc.measure(600)
            print(f'{i}-th pnts = {pnts}')
            for p in pnts:
                bh = MkCircle(Ge.Point3d(p[0],p[1],0),Ge.Vector3d(0,0,1),Ge.Vector3d(1,0,0),50)
                bh.Color.setRGB(0,255,0)
                tunnel.addBlasthole(bh)
            tunnel.addArc(arc)
        
        tunnel.appendDb(model)

    except Exception as err:
        print(err)

def PyRxCmd_tun():
    pass