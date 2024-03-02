# under construction, this module depends on MkTunnel, MkBlast and Lib classes

import PyRx as Rx
import PyGe as Ge
import PyGi as Gi
import PyDb as Db
import PyAp as Ap
import PyEd as Ed
import math
import json
from lib import *


class dBBaseHoles():
    def __init__(self):
        self.json = {}
        self.Holes = [] # list of MkBlastHoles
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json
    
class dBCenterHoles(dBBaseHoles):
    def __init__(self):
        self.json = {}
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json
    
class dBOutterHoles(dBBaseHoles):
    def __init__(self):
        self.json = {}
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json
    
class dbFloorHoles(dBBaseHoles):
    def __init__(self):
        self.json = {}
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json
    
class dbInnerHoles(dBBaseHoles):
    def __init__(self):
        self.json = {}
        
    def add(self, key, value):
        self.json[key] = value

    def dump(self):
        return json.dumps(self.json)
        
    def get(self):
        return self.json
    

