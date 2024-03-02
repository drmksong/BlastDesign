# this module contains classes specific to blast hole design and layout
from typing import Any
from lib import *

def OnPyInitApp():
    print("\nOnPyRx MkBlast")
    print("\ncommand = blatst")
    # manager.addPointMonitor(pm)    


class enumChargeCurveType(Enum):
    Line = 1
    Arc = 2

class enumBlastHoleType(Enum):
    EmptyHole = 0
    CenterCutHole = 1
    StoppingHole = 2
    FloorHole = 3
    SmoothBlastHole = 4


class enumCutHoleType(Enum):
    EmptyHole = 0
    FirstCut = 1
    SecondCut = 2
    ThirdCut = 3
    FourthCut = 4


class enumStoppingHoleType(Enum):
    Upward = 1
    Downward = 2


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

class enumDetonatorType(Enum):
    NoneDetonator = 0
    Electric = 1
    NonElectric_MS = 11
    NonElectric_LP = 12
    Electronic = 20

class ExplosiveDict(dict):
    def __setitem__(self, __key: Any, __value: Any) -> None:
        if enumExplosiveType.is_Explosive(__key):
            super().__setitem__(enumExplosiveType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid explosive type: {__key}")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, str):
            __key = enumExplosiveType(__key.upper())
        return super().__getitem__(__key)
        

class MkBlastHole(MkCircle):
    def __init__(self, cen=Ge.Point3d(0, 0, 0), norm=Ge.Vector3d(0, 0, 1), ref=Ge.Vector3d(1, 0, 0), rad=1000):
        super().__init__(cen, norm, ref, rad)
        self.NumCartrige = ExplosiveDict() # dictionary of numbers of cartrige of different explosive types, mostly emulsion and finex ex {"ANFO":0, "Emulsion":0, "Dynamite":0, "Finex":0}
        self.BlastHoleType = ExplosiveDict() # enumBlastHoleType ex {"HoleType":enumCutHoleType.EmptyHole}
        # self.CutHoleType = "" # valid only if self.BlastHoleType is CutHole
        # self.StoppingHoleType = "" # valid only if self.BlastHoleType is StoppingHole
        self.ExplosiveTypes = [] # list of enumExplosiveType [enumExplosiveType, enumExplosiveType, ...]
        self.ChargeWeights = ExplosiveDict() # list of charge weights of different explosive types
        self.DetonatorType = enumDetonatorType.NoneDetonator # enumDetonatorType 
        self.ParentChargeCurve = MkChargeCurve() # master line of the blast hole
        self.TotalLength = 0.0 # total length of the blast hole
        self.TampingLength = 0.0 # tamping length of the blast hole
        self.ChargedLength = 0.0 # charge length of the blast hole

class MkCenterCutHoles():
    def __init__(self):
        self.CenterCutHoles = [] # list of MkBlastHole
        self.EmptyHoleRadius = 102.0 # radius of the empty hole, default 102.0mm
        self.EmptyHoleNumber = 3 # number of empty holes


class MkBlastHoles():
    def __init__(self):
        self.BlastHoles = [] # list of MkBlastHole
        self.BlastHoleRadius = 45.0 # radius of the blast hole, default 45.0mm        

class MkChargeCurve(MkLine,MkArc): # inherit from MkLine and MkArc for the layout of blast holes 
    def __init__(self, curveType):
        self.Curve = MkLine() # default curve is a line
        self.CurveType = curveType # enumChargeCurveType
        if self.CurveType == enumChargeCurveType.Line:
            self.Curve = MkLine()
        elif self.CurveType == enumChargeCurveType.Arc:
            self.Curve = MkArc()
        self.BlastHoles = MkBlastHoles() # list of MkBlastHole class     

class MkChargeCurves():
    def __init__(self):
        self.ChargeCurves = [MkChargeCurve()] # list of MkChargeCurve class





def PyRxCmd_blatst():
    try:
        ed = ExplosiveDict()
        ed[enumExplosiveType.ANFO] = 10
        ed['ANFO']+=1
        ed['Dynamite'] = 5

        ed[enumExplosiveType.Emulsion] = 1
        # ed[enumExplosiveType.ANFO] = 1
        # print(ed[enumExplosiveType.ANFO])
        print(ed)
    except Exception as e:
        print(e)