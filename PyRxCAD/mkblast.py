# this module contains classes specific to blast hole design and layout
from typing import Any
from plum import dispatch
from lib import *


def OnPyInitApp():
    print("\nOnPyRx MkBlast")
    print("\ncommand = blatst")
    # manager.addPointMonitor(pm)    


#######################
class enumCenterCutType(Enum): # this enum is for tunnel face type of center cut, member of Tunnel class
    Parallel = "Parallel"
    Wedge = "Wedge"

    @classmethod
    def is_CenterCut(cls, centerCutType):
        if isinstance(centerCutType, cls):
            centerCutType = centerCutType.value
        if not centerCutType in cls.__members__:
            return False
        else:
            return True

class CenterCutTypeDict(dict): # dictionary of center cut enum types and their string literals
    def __setitem__(self, __key: Any, __value: Any) -> None:
        if enumCenterCutType.is_CenterCut(__key):
            super().__setitem__(enumCenterCutType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid center cut type: {__key}")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, Any):
            __key = enumCenterCutType(__key.upper())
        return super().__getitem__(__key)

#######################
    
class enumBlastHoleType(Enum):
    EmptyHole = 'EmptyHole'
    CenterCutHole = 'CenterCutHole'
    StoppingHole = 'StoppingHole'
    FloorHole = 'FloorHole'
    SmoothBlastHole = 'SmoothBlastHole'

    @classmethod
    def is_BlastHole(cls, blastHoleType):
        if isinstance(blastHoleType, cls):
            blastHoleType = blastHoleType.value
        if not blastHoleType in cls.__members__:
            return False
        else:
            return True

class BlastHoleTypeDict(dict): # dictionary of blast hole enum types and their string literals, need to revise for checking cut hole should be cut hole and stopping hole should be stopping hole
    def __setitem__(self, __key: Any, __value: Any) -> None:
        if len(self) ==0 and enumBlastHoleType.is_BlastHole(__key) and \
          (enumCutHoleType.is_CutHole(__value) or \
           enumStoppingHoleType.is_StoppingHole(__value) or \
           enumBlastHoleType.is_BlastHole(__value)):
            super().__setitem__(enumBlastHoleType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid blast hole type: {__key} or {len(self)} exceeds 1")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, str):
            __key = enumBlastHoleType(__key.upper())
        return super().__getitem__(__key)

#######################        

class enumCutHoleType(Enum):
    EmptyHole = 'EmptyHole'
    FirstCut = 'FirstCut'
    SecondCut = 'SecondCut'
    ThirdCut = 'ThirdCut'
    FourthCut = 'FourthCut'

    @classmethod
    def is_CutHole(cls, cutHoleType):
        if isinstance(cutHoleType, cls):
            cutHoleType = cutHoleType.value
        if not cutHoleType in cls.__members__:
            return False
        else:
            return True

# delete if it is not necessary
# class CutHoleType(): # dictionary of center cut hole enum types and their string literals
#     def __setitem__(self, __value: str) -> None:
#         if enumCutHoleType.is_CutHole(__value):
#             super().__setitem__(__value)
#         else:
#             raise KeyError(f"setter::Invalid cut hole type: {__value}")

#     def __getitem__(self) -> Any:
#         return super().__getitem__()

#######################

class enumStoppingHoleType(Enum):
    Upward = 'Upward'
    Downward = 'Downward'

    @classmethod
    def is_StoppingHole(cls, stoppingHoleType):
        if isinstance(stoppingHoleType, cls):
            stoppingHoleType = stoppingHoleType.value
        if not stoppingHoleType in cls.__members__:
            return False
        else:
            return True

class StoppingHoleDict(dict): # dictionary of stopping hole enum types and their string literals
    def __setitem__(self, __key: Any, __value: str) -> None:
        if enumStoppingHoleType.is_StoppingHole(__key):
            super().__setitem__(enumStoppingHoleType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid stopping hole type: {__key}")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, str):
            __key = enumStoppingHoleType(__key.upper())
        return super().__getitem__(__key)

#######################

class enumExplosiveType(Enum):
    NonExplosive = "NonExplosive"
    ANFO = "ANFO"
    Emulsion = "Emulsion"
    Dynamite = "Dynamite"
    Finex = "Finex"

    @classmethod
    def is_Explosive(cls, explosiveType):
        if isinstance(explosiveType, cls):
            explosiveType = explosiveType.value
        if not explosiveType in cls.__members__:
            return False
        else:
            return True

class ExplosiveDict(dict): # dictionary of explosive enum types and their string literals
    def __setitem__(self, __key: Any, __value: str) -> None:
        if enumExplosiveType.is_Explosive(__key):
            super().__setitem__(enumExplosiveType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid explosive type: {__key}")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, str):
            __key = enumExplosiveType(__key.upper())
        return super().__getitem__(__key)
        
#######################
    
class enumDetonatorType(Enum):
    NoneDetonator = 'NoneDetonator'
    Electric = 'Electric'
    NonElectric_MS = 'NonElectric_MS'
    NonElectric_LP = 'NonElectric_LP'
    Electronic = 'Electronic'

    @classmethod
    def is_Detonator(cls, detonatorType):
        if isinstance(detonatorType, cls):
            detonatorType = detonatorType.value
        if not detonatorType in cls.__members__:
            return False
        else:
            return True

class Detonator():
    def __init__(self, detonatorType:enumDetonatorType=enumDetonatorType.NoneDetonator, detonatorDelay:float=0.0, detonatorNumber:int=0):
        self.DetonatorType = enumDetonatorType.NoneDetonator # enumDetonatorType 
        self.DetonatorDelay = detonatorDelay
        self.DetonatorNumber = detonatorNumber

    def __repr__(self):
        return f"DetonatorType: {self.DetonatorType}, DetonatorDelay: {self.DetonatorDelay}, DetonatorNumber: {self.DetonatorNumber}"
    
class DetonatorDict(dict): # dictionary of explosive enum types and their string literals
    def __setitem__(self, __key: Any, __value: Detonator) -> None:
        if type(__key) is int:
            super().__setitem__(__key, __value)

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, int):
            return super().__getitem__(__key)
        else: return None

class Detonators():
    def __init__(self):
        self.Detonators = DetonatorDict() # dictionary of Detonator class

    def __getitem__(self, __key: Any) -> Any:
        return self.Detonators[__key]
    
    def __setitem__(self, __key: Any, __value: Detonator) -> None:
        self.Detonators[__key] = __value

#######################
        
class MkBlastHole(MkCircle):
    def __init__(self, cen=Ge.Point3d(0, 0, 0), norm=Ge.Vector3d(0, 0, 1), ref=Ge.Vector3d(1, 0, 0), rad=1000):
        super().__init__(cen, norm, ref, rad)
        self.NumCartrige = ExplosiveDict() # dictionary of numbers of cartrige of different explosive types, mostly emulsion and finex ex {"ANFO":0, "Emulsion":0, "Dynamite":0, "Finex":0}
        self.BlastHoleType = BlastHoleTypeDict() # enumBlastHoleType ex {"HoleType":enumCutHoleType.EmptyHole}
        # self.CutHoleType = "" # valid only if self.BlastHoleType is CutHole
        # self.StoppingHoleType = "" # valid only if self.BlastHoleType is StoppingHole
        self.ExplosiveTypes = [] # list of enumExplosiveType [enumExplosiveType.Emulsion, enumExplosiveType.Finex, ...]
        self.ChargeWeights = ExplosiveDict() # list of charge weights of different explosive types
        self.Detonators = DetonatorDict() # dictionary of detonators of different types
        # self.DetonatorType = enumDetonatorType.NoneDetonator # enumDetonatorType 
        # self.DetonatorDelay = 0.0
        self.ParentChargeCurve = 0 # id of charge line or arc of the blast hole 
        self.TotalLength = 0.0 # total length of the blast hole
        self.Lengths = ExplosiveDict() # dictionary of lengths of tamping and different explosive types, 
        
class MkBlastHoleDict(dict): # dictionary of blast holes
    def __setitem__(self, __key: int, __value: MkBlastHole) -> None:
        if isinstance(__value, MkBlastHole):
            super().__setitem__(__key, __value)
        else:
            raise ValueError(f"setter::Invalid value type: {type(__value)}")

    def __getitem__(self, __key: int) -> Any:
        return super().__getitem__(__key)


class MkCenterCutHoles():
    def __init__(self):
        self.CenterCutHoles = MkBlastHoleDict() # dictionary of MkBlastHoleDict
        self.EmptyHoleRadius = 102.0 # radius of the empty hole, default 102.0mm
        self.EmptyHoleNumber = 3 # number of empty holes
    
    def __getitem__(self, __key: Any) -> Any:
        return self.CenterCutHoles[__key]
    
    def __setitem__(self, __key: Any, __value: MkBlastHole) -> None:
        bh = __value
        bh.Radius = self.EmptyHoleRadius
        self.CenterCutHoles[__key] = __value

class MkBlastHoles():
    def __init__(self):
        self.BlastHoles = MkBlastHoleDict() # dictionary of MkBlastHoleDict
        self.BlastHoleRadius = 45.0 # radius of the blast hole, default 45.0mm        

    def __getitem__(self, __key: Any) -> Any:
        return self.BlastHoles[__key]
    
    def __setitem__(self, __key: Any, __value: MkBlastHole) -> None:
        bh = __value
        bh.Radius = self.BlastHoleRadius
        self.BlastHoles[__key] = __value

#######################
class enumChargeCurveType(Enum):
    Line = 'Line' 
    Arc = 'Arc'

    @classmethod
    def is_ChargeCurve(cls, chargeCurveType):
        if isinstance(chargeCurveType, cls):
            chargeCurveType = chargeCurveType.value
        if not chargeCurveType in cls.__members__:
            return False
        else:
            return True

class MkChargeCurve(MkLine,MkArc): # inherit from MkLine and MkArc for the layout of blast holes 
    @dispatch
    def __init__(self, curveType:enumChargeCurveType=enumChargeCurveType.Line):
        self.CurveType = curveType # enumChargeCurveType
        if self.CurveType == enumChargeCurveType.Line:
            self.Curve = MkLine()
        elif self.CurveType == enumChargeCurveType.Arc:
            self.Curve = MkArc()
        self.BlastHoles = MkBlastHoles() # dictionary of MkBlastHole class     
    @dispatch
    def __init__(self, curve:MkLine):
        self.CurveType = enumChargeCurveType.Line
        self.Curve = curve
        self.BlastHoles = MkBlastHoles()
    @dispatch
    def __init__(self, curve:MkArc):
        self.CurveType = enumChargeCurveType.Arc
        self.Curve = curve
        self.BlastHoles = MkBlastHoles()    


class ChargeCurveDict(dict): # dictionary of explosive enum types and their string literals
    def __setitem__(self, __key: int, __value: MkChargeCurve) -> None:
        # if enumChargeCurveType.is_ChargeCurve(__key):
        if type(__key)==int:
            super().__setitem__(__key, __value)
        else:
            raise KeyError(f"setter::Invalid charge curve type: {__key}")

    def __getitem__(self, __key: int) -> Any:
        if isinstance(__key, int):
            return super().__getitem__(__key)
        else: return None


class MkChargeCurves():
    def __init__(self):
        self.ChargeCurves = ChargeCurveDict() # list of MkChargeCurve class

#######################



def PyRxCmd_blatst():
    try:
        db = Db.HostApplicationServices().workingDatabase()
        model = Db.BlockTableRecord(db.modelSpaceId(), Db.OpenMode.ForWrite)

#----------------------
        ed = ExplosiveDict()
        ed[enumExplosiveType.ANFO] = 10
        ed['ANFO']+=1
        ed['Dynamite'] = 5

        ed[enumExplosiveType.Emulsion] = 1
        # ed[enumExplosiveType.ANFO] = 1
        # print(ed[enumExplosiveType.ANFO])
        print(ed)

#----------------------
        line = MkLine(Ge.Point3d(0, 0, 0), Ge.Point3d(1000, 0, 0))
        arc = MkArc(Ge.Point3d(0, 0, 0), Ge.Vector3d(0, 0, 1), Ge.Vector3d(1, 0, 0), 1000, 0, 90*3.14159/180)        

        cc = MkChargeCurves()   
        cc.ChargeCurves[1] = MkChargeCurve(line)
        cc.ChargeCurves[2] = MkChargeCurve(arc)
        
        for k,c in cc.ChargeCurves.items():
            c.Curve.appendDb(model)
            print(f'[{k}]-th {c.Curve.Type} is appended to the model space')

        # for k,c in cc.ChargeCurves:
        #     c.AppendDb(model)
        #     print(f'[{k}]-th {c.Curve.Type} is appended to the model space')
#----------------------
        bh = MkBlastHole(Ge.Point3d(0, 500, 0), Ge.Vector3d(0, 0, 1), Ge.Vector3d(1, 0, 0), 1000)
        bh2 = MkBlastHole(Ge.Point3d(0, -500, 0), Ge.Vector3d(0, 0, 1), Ge.Vector3d(1, 0, 0), 1000)
        ch = MkBlastHole(Ge.Point3d(500, 0, 0), Ge.Vector3d(0, 0, 1), Ge.Vector3d(1, 0, 0), 1000)
        ch2 = MkBlastHole(Ge.Point3d(-500, 0, 0), Ge.Vector3d(0, 0, 1), Ge.Vector3d(1, 0, 0), 1000)
        bhs = MkBlastHoles()
        chs = MkCenterCutHoles()

        bhs[1] = bh
        bhs[2] = bh2
        chs[1] = ch
        chs[2] = ch2

        for k,b in bhs.BlastHoles.items():
            b.appendDb(model)
            print(f'[{k}]-th blast hole is appended to the model space')

        for k,c in chs.CenterCutHoles.items():
            c.appendDb(model)
            print(f'[{k}]-th center cut hole is appended to the model space')
#----------------------
        det = Detonators()
        det[1] = Detonator()
        det[2] = Detonator()

        det[1].DetonatorType = enumDetonatorType.NonElectric_LP
        det[1].DetonatorDelay = 10.0
        det[1].DetonatorNumber = 1

        det[2].DetonatorType = enumDetonatorType.NonElectric_MS
        det[2].DetonatorDelay = 20.0
        det[2].DetonatorNumber = 2

        for k,d in det.Detonators.items():
            print(f'[{k}]-th detonator is {d}')

#----------------------
        btd = BlastHoleTypeDict()
        btd[enumBlastHoleType.CenterCutHole] = enumCutHoleType.FirstCut
        print(btd.items())
        btd.clear()
        print(f'bed is cleared: {btd}')
        btd[enumBlastHoleType.SmoothBlastHole] = enumBlastHoleType.SmoothBlastHole
        print(btd[enumBlastHoleType.SmoothBlastHole])



    except Exception as e:
        print(e)