import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
import math
import pandas as pd


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
    def __init__(self,cen=Ge.Point3d(0, 0, 0),norm=Ge.Vector3d(0, 0, 1),ref=Ge.Vector3d(1, 0, 0),rad=1000):
        self.Center = cen
        self.Norm = norm
        self.Ref = ref
        self.Radius = rad
        self.Circle = Db.Arc()
        self.Color = Db.Color()
    
    def setRadius(self, r:float):
        self.Radius = r

    def setCenter(self, c:Ge.Point3d):
        self.Center = c

    def setNorm(self, n:Ge.Vector3d):
        self.Norm = n

    def setRef(self, r:Ge.Vector3d):    
        self.Ref = r                

    def setColor(self, c:Db.Color):
        self.Color = c

    def convDb(self)->Db.Arc:
        self.Circle = Db.Arc(self.Center,self.Norm,self.Radius,0,2*3.141592)
        self.Circle.setColor(self.Color)
        return self.Circle

    def measure(self,space:float)->list:
        N = self.Radius*(self.EndAngle-self.StartAngle)/space
        theta = space/self.Radius
        print(f'N = {N}, theta = {theta}')

        return [
            (self.Radius*math.cos(self.StartAngle+theta*float(i))+self.Center[0],
             self.Radius*math.sin(self.StartAngle+theta*float(i))+self.Center[1]) 
            for i in range(round(N))
        ]

    def measureN(self,n:int)->list:
        theta = (self.EndAngle-self.StartAngle)/n
        print(f'N = {n}, theta = {theta}')

        return [
            (self.Radius*math.cos(self.StartAngle+theta*float(i))+self.Center[0],
             self.Radius*math.sin(self.StartAngle+theta*float(i))+self.Center[1]) 
            for i in range(n)
        ]
    def appendDb(self,model:Db.BlockTableRecord):
        self.convDb()
        model.appendAcDbEntity(self.Circle)

class MkArc(MkCircle):
    def __init__(self,cen=Ge.Point3d(0, 0, 0),norm=Ge.Vector3d(0, 0, 1),ref=Ge.Vector3d(1, 0, 0),rad=1000,start=0,end=2*3.141592):
        super().__init__(cen,norm,ref,rad)
        self.StartAngle = start
        self.EndAngle = end
        self.Start = Ge.Point3d(self.Radius*math.cos(self.StartAngle)+self.Center[0],self.Radius*math.sin(self.StartAngle)+self.Center[1],0)
        self.End = Ge.Point3d(self.Radius*math.cos(self.EndAngle)+self.Center[0],self.Radius*math.sin(self.EndAngle)+self.Center[1],0)
        
        v1 = Ge.Vector2d(self.Start[0]-self.Center[0],self.Start[1]-self.Center[1])
        v2 = Ge.Vector2d(self.Start[0]-self.End[0],self.Start[1]-self.End[1])
        a=(v1.angleTo(v2))
        self.Verge = math.tan(math.pi/2+a) if a > math.pi/2 else math.tan((math.pi/2-a)/2)
        self.Arc = Db.Arc()
    
    def setRadius(self, r:float):
        super().setRadius(r)
        self.Start = Ge.Point3d(self.Radius*math.cos(self.StartAngle)+self.Center[0],self.Radius*math.sin(self.StartAngle)+self.Center[1],0)
        self.End = Ge.Point3d(self.Radius*math.cos(self.EndAngle)+self.Center[0],self.Radius*math.sin(self.EndAngle)+self.Center[1],0)

        
    def setCenter(self, c:Ge.Point3d):
        super().setCenter(c)
        self.Start = Ge.Point3d(self.Radius*math.cos(self.StartAngle)+self.Center[0],self.Radius*math.sin(self.StartAngle)+self.Center[1],0)
        self.End = Ge.Point3d(self.Radius*math.cos(self.EndAngle)+self.Center[0],self.Radius*math.sin(self.EndAngle)+self.Center[1],0)

        
    def setStartAngle(self, a:float): # a is in radians
        self.StartAngle = a
        self.Start = Ge.Point3d(self.Radius*math.cos(self.StartAngle)+self.Center[0],self.Radius*math.sin(self.StartAngle)+self.Center[1],0)
        self.End = Ge.Point3d(self.Radius*math.cos(self.EndAngle)+self.Center[0],self.Radius*math.sin(self.EndAngle)+self.Center[1],0)


    def setEndAngle(self, a:float): # a is in radians
        self.EndAngle = a
        self.Start = Ge.Point3d(self.Radius*math.cos(self.StartAngle)+self.Center[0],self.Radius*math.sin(self.StartAngle)+self.Center[1],0)
        self.End = Ge.Point3d(self.Radius*math.cos(self.EndAngle)+self.Center[0],self.Radius*math.sin(self.EndAngle)+self.Center[1],0)


    def convDb(self)->Db.Arc:
        self.Arc = Db.Arc(self.Center,self.Norm,self.Radius,self.StartAngle,self.EndAngle)
        self.Arc.setColor(self.Color)
        return self.Arc
    
    def measure(self,space:float)->list: # list of points, not Ge.Point3d so that you much convert it to Ge.Point3d
        if self.StartAngle > self.EndAngle:
            self.StartAngle -= 2*3.141592

        N = self.Radius*(self.EndAngle-self.StartAngle)/space
        theta = space/self.Radius
        print(f'N = {N}, theta = {theta}, sang={self.StartAngle}, eang={self.EndAngle}')

        return [
            (self.Radius*math.cos(self.StartAngle+theta*float(i))+self.Center[0],
             self.Radius*math.sin(self.StartAngle+theta*float(i))+self.Center[1]) 
            for i in range(round(N))
        ]

    def appendDb(self,model:Db.BlockTableRecord):
        # self.convDb()
        self.Arc = Db.Arc(self.Center,self.Norm,self.Radius,self.StartAngle,self.EndAngle)
        model.appendAcDbEntity(self.Arc)


class MkLine():
    def __init__(self,start=Ge.Point3d(0, 0, 0),end=Ge.Point3d(0, 0, 0)):
        self.Start = start
        self.End = end
        self.Length = self.Start.distanceTo(self.End)
        self.Line = Db.Line()
        self.Color = Db.Color()

    def setStart(self, s:Ge.Point3d):
        self.Start = s
        self.Length = self.Start.distanceTo(self.End)

    def setEnd(self, e:Ge.Point3d):    
        self.End = e
        self.Length = self.Start.distanceTo(self.End)

    def setColor(self, c:Db.Color):
        self.Color = c

    def convDb(self)->Db.Line:
        self.Line = Db.Line(self.Start,self.End)
        self.Line.setColor(self.Color)
        return self.Line
    
    def measure(self,space:float)->list: # list of points, not Ge.Point3d so that you much convert it to Ge.Point3d
        N = (self.Length/space)
        s = self.Start
        e = self.End
        return [
            ((e[0]-s[0])*float(i)/N+s[0],
             (e[1]-s[1])*float(i)/N+s[1]) 
            for i in range(round(N))
        ]
    
    def scale(self,sc:float):
        m = [(self.Start[0]+self.End[0])/2,(self.Start[1]+self.End[1])/2]
        s = self.Start
        e = self.End

        self.Start = Ge.Point3d(m[0]+sc*(s[0]-m[0]),m[1]+sc*(s[1]-m[1]),0)
        self.End   = Ge.Point3d(m[0]+sc*(e[0]-m[0]),m[1]+sc*(e[1]-m[1]),0)
    
    # edge is the length of the edge to be trimmed
    def trimEdge(self,edge:float):
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
    def offset(self,off:float,dir:int)->'MkLine':
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

    def appendDb(self,model:Db.BlockTableRecord):
        self.convDb()
        model.appendAcDbEntity(self.Line)


class MkPolyLine():
    def __init__(self):
        # self.Center = Ge.Point3d(0, 0, 0)
        self.Arcs = []
        self.Lines = []
        self.Polyline = Db.Polyline()
        self.pnts = []
        self.rads = []
        self.verges = []
        self.Color = Db.Color()

        
    def addArc(self,a:MkArc):
        self.Arcs.append(a)
        st = Ge.Point2d(a.Start[0],a.Start[1])
        ed = Ge.Point2d(a.End[0],a.End[1])
        if len(self.pnts)>0:
            print(f'\n *** distance = {st.distanceTo(self.pnts[-1])}')
            if st.distanceTo(self.pnts[-1]) < 1:
                print(f'valid self.pnts[-1] = {self.pnts[-1]}, a.Start = {st}')
                print('Valid Line, append operation')
                self.pnts.append(ed)
                self.rads.append(a.Radius)
                self.verges.append(a.Verge)
            elif st.distanceTo(self.pnts[-1]) > 1:
                print(f'invalid self.pnts[-1] = {self.pnts[-1]}, a.Start = {st}')
                print('Invalid Line, arbort operation')
                # exit(-1)
            else:
                pass
            if ed.distanceTo(self.pnts[0]) < 10:
                print(f'valid self.pnts[0] = {self.pnts[-1]}, a.End = {ed}')
                print('Valid Line, append operation')
                self.rads.append(a.Radius)
                self.verges.append(a.Verge)
            
        else:
            print('First Arc')
            self.pnts.append(st)
            self.rads.append(a.Radius)
            self.verges.append(a.Verge)
            self.pnts.append(ed)
            # self.rads.append(a.Radius)
            # self.verges.append(a.Verge)   
        

    def addLine(self,l):
        self.Lines.append(l)
        st = Ge.Point2d(l.Start[0],l.Start[1])
        ed = Ge.Point2d(l.End[0],l.End[1])
        if len(self.pnts)>0:
            if self.pnts[-1] == st:
                print(f'valid self.pnts[-1] = {self.pnts[-1]}, l.Start = {st}')
                print('Valid Line, append operation')
                self.pnts.append(ed)
                self.rads.append(0.0)
                self.verges.append(0.0)
            else:
                print(f'invalid self.pnts[-1] = {self.pnts[-1]}, l.Start = {st}')
                print('Invalid Line, arbort operation')
                # exit(-1)
        else:
            self.pnts.append(st)
            self.rads.append(0.0)
            self.verges.append(0.0)
            self.pnts.append(ed)
            self.rads.append(0.0)
            self.verges.append(0.0)   

    def setColor(self, c:Db.Color):
        self.Color = c


    def buildPoly(self,debug=False):
        try:
            assert len(self.pnts) == len(self.rads) == len(self.verges)
            if debug:
                print(f'pnts = {self.pnts}, rads = {self.rads}, verges = {self.verges}')

            gepnts = [Ge.Point2d(self.pnts[i][0],self.pnts[i][1]) for i in range(len(self.pnts))]

            self.Polyline.setDatabaseDefaults()
            for i in range(len(self.pnts)):
                self.Polyline.addVertexAt(i,self.pnts[i], self.verges[i], 0, 0)
            self.Polyline.setClosed(True)

            # color = Db.Color()
            # color.setRGB(255, 0, 255)
            self.Polyline.setColor(self.Color)

        except Exception as err:
            print(err)  


    def appendDb(self,model:Db.BlockTableRecord,debug=False): # build Polyline has to be done earlier ***
        if debug:
            for a in self.Arcs:
                print(a)
                a.appendDb(model)
            for l in self.Lines:
                print(l)
                l.appendDb(model)
        model.appendAcDbEntity(self.Polyline)


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

class MkBlastLine(MkLine):
    pass

class MkBlastArc(MkArc):    
    pass

class MkTunnel():
    def __init__(self):
        self.Profile = MkTunnelProfile()
        self.Lines = [] # list of MkLine
        self.Arcs = [] # list of MkArc
        self.Blasthole = [] # list of MkCircle
        
    def addBlasthole(self,bh:MkCircle):
        self.Blasthole.append(bh)

    def addLine(self,l:MkLine):
        self.Lines.append(l)

    def addArc(self, a:MkArc):
        self.Arcs.append(a)

    def appendDb(self,model:Db.BlockTableRecord,debug=False):
        for a in self.Arcs:
            if debug: print(a)
            a.appendDb(model)
        for l in self.Lines:
            if debug: print(l)
            l.appendDb(model)
        for bh in self.Blasthole:
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
        # cirs = [MkArc(Ge.Point3d(res[i][0],res[i][1],0),norm,ref,rad,0,359) for i in range(len(res))]
        cirs = [MkArc(c,norm,ref,rad) for c in cen]

        # print(cirs)
        for c in cirs:
            c.appendDb(model)

        # rad = 100
        # cen = Ge.Point3d(0,-200,0)
        # tun1 = MkArc(cen,norm,ref,rad,-30*3.14159/180,90*3.14159/180)
        # tun2 = MkArc(cen,norm,ref,rad,90*3.14159/180,210*3.14159/180)
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

        # cirs = [MkArc(c,norm,ref,rad) for c in cen]
        # cirs2 = [MkArc(c,norm,ref,rad) for c in cen2]

        # for c in cirs:
        #     c.appendDb(model)
        # for c in cirs2:
        #     c.appendDb(model)


    except Exception as err:
        print(err)


