from mklib import *


class MkPoly(MkObj):
    def __init__(self,parent=None):
        super().__init__()
        self.classname = 'MkPoly'
        self.poly = [] 

    # it is not yet tested, need strict testing    
    def add(self,obj: MkObj):
        if obj.classname == 'MkPoint':
            mkobj = MkPoint(obj)
        self.poly.append(mkobj)





