# import clr

# path = 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\'

# clr.AddReferenceToFileAndPath(path + 'acdbmgd.dll')
# clr.AddReferenceToFileAndPath(path + 'acmgd.dll')
# clr.AddReferenceToFileAndPath(path + 'acmgdinternal.dll')
 

# import Autodesk
# import Autodesk.AutoCAD.Runtime as ar
# import Autodesk.AutoCAD.ApplicationServices as aas
# import Autodesk.AutoCAD.DatabaseServices as ads
# import Autodesk.AutoCAD.Geometry as ag
# import Autodesk.AutoCAD.Internal as ai
# from Autodesk.AutoCAD.Internal import Utils


import sys, clr 
clr.AddReference('ProtoGeometry')
import Autodesk
from Autodesk.DesignScript.Geometry import *
from math import tan, radians
