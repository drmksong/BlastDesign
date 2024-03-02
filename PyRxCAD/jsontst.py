# disregard this file, it is for testing purposes only

# Obsoleted: Yes
# Throw away file

import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
import math
import json

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

class MkJson():
    def __init__(self):
        self.json = {}
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json


def PyRxCmd_tst():
    print("\nPyRxCmd_tst")

    jstr = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print(jstr)    
    mk = MkJson()
    mk.add('name', 'circle')
    mk.add('center', Ge.Point3d(0, 0, 0))
    mk.add('norm', Ge.Vector3d(0, 0, 1))
    # jsonstr = mk.dump()
    print(mk.json)
