import math
from misc import *
from charge import *


class StopingPR(OutCut):
    def __init__(self):
        super().__init__()
        self.__name__ = "STOPING"

    @property
    def name(self):
        print(f'my name is stoping')
        return self.__name__

    @name.setter
    def name(self, name: str):
        self.__name__ = name

    def calc(self, W: float):
        self.cut.B = min(1, W)
        self.cut.h0 = 0.5 * self.cut.B

        self.cut.hb = self.cut.B / 3
        self.cut.Ib = self.cut.IExp.Ic
        self.cut.Qb = self.cut.Ib*(self.cut.hb)

        self.cut.nb = rnd(self.cut.Qb / (self.cut.IExp.wei))
        self.cut.Qba = self.cut.nb * self.cut.IExp.wei

        self.cut.Ic = self.cut.Ib 
        self.cut.Qc = self.cut.Ic*(self.cut.H - self.cut.h0 - self.cut.hb)

        self.cut.nc = rnd(self.cut.Qc / (self.cut.IExp.wei))
        self.cut.Qca = self.cut.nc * self.cut.IExp.wei

        self.cut.Qtot = self.cut.Qca + self.cut.Qba
        self.cut.W = 0
        self.cut.L = self.cut.h0 + \
            (self.cut.nb+self.cut.nc) * self.cut.IExp.len
        if self.cut.L > self.cut.H * 1.0:
            n = rnd((self.cut.L - self.cut.H)/self.cut.IExp.len)
            self.cut.nc = self.cut.nc - n
            self.cut.L = self.cut.h0 + \
                (self.cut.nb+self.cut.nc) * self.cut.IExp.len
            self.cut.Qca = self.cut.nc * self.cut.IExp.wei
            self.cut.Qtot = self.cut.Qca + self.cut.Qba


class FloorPR(OutCut):
    def __init__(self):
        super().__init__()
        self.__name__ = "FLOOR"

    @property
    def name(self):
        print(f'my name is floor')
        return self.__name__

    @name.setter
    def name(self, name: str):
        self.__name__ = name

    def calc(self, W):
        self.cut.B = min(1, W)
        self.cut.h0 = 0.2 * self.cut.B

        self.cut.hb = self.cut.B / 3
        self.cut.Ib = self.cut.IExp.Ic
        self.cut.Qb = self.cut.Ib*(self.cut.hb)

        self.cut.nb = rnd(self.cut.Qb / (self.cut.IExp.wei))
        self.cut.Qba = self.cut.nb * self.cut.IExp.wei

        self.cut.Ic = self.cut.Ib / 1
        self.cut.Qc = self.cut.Ic*(self.cut.H - self.cut.h0 - self.cut.hb)

        self.cut.nc = rnd(self.cut.Qc / (self.cut.IExp.wei))
        self.cut.Qca = self.cut.nc * self.cut.IExp.wei

        self.cut.Qtot = self.cut.Qca + self.cut.Qba
        self.cut.W = 0
        self.cut.L = self.cut.h0 + \
            (self.cut.nb+self.cut.nc) * self.cut.IExp.len

        if self.cut.L > self.cut.H * 1.0:
            n = rnd((self.cut.L - self.cut.H)/self.cut.IExp.len)
            self.cut.nc = self.cut.nc - n
            self.cut.L = self.cut.h0 + \
                (self.cut.nb+self.cut.nc) * self.cut.IExp.len
            self.cut.Qca = self.cut.nc * self.cut.IExp.wei
            self.cut.Qtot = self.cut.Qca + self.cut.Qba


class PerimPR(OutCut):
    def __init__(self):
        super().__init__()
        self.__name__ = "PERIM"

    @property
    def name(self):
        print(f'my name is perimeter hole')
        return self.__name__

    @name.setter
    def name(self, name: str):
        self.__name__ = name

    def calc(self, W: float):
        self.cut.B = min(0.8, rnd(W*0.8, 1))
        self.cut.h0 = 0.5 * self.cut.B

        self.cut.hb = self.cut.B / 3
        self.cut.Ib = self.cut.IExp.Ic
        self.cut.Qb = self.cut.Ib*(self.cut.hb)

        self.cut.nb = rnd(self.cut.Qb / (self.cut.IExp.wei))
        self.cut.Qba = self.cut.nb * self.cut.IExp.wei

        self.cut.Ic = self.cut.OExp.Ic
        self.cut.Qc = self.cut.Ic*(self.cut.H - self.cut.h0 - self.cut.hb)

        self.cut.nc = rnd(self.cut.Qc / (self.cut.OExp.wei))
        self.cut.Qca = self.cut.nc * self.cut.OExp.wei

        self.cut.Qtot = self.cut.Qca + self.cut.Qba
        self.cut.W = 0
        self.cut.L = self.cut.h0 + \
            (self.cut.nb) * self.cut.IExp.len + \
            (self.cut.nc) * self.cut.OExp.len

        if self.cut.L > self.cut.H * 1.0:
            n = rnd((self.cut.L - self.cut.H)/self.cut.OExp.len)
            self.cut.nc = self.cut.nc - n
            self.cut.L = self.cut.h0 + \
                (self.cut.nb) * self.cut.IExp.len + \
                (self.cut.nc) * self.cut.OExp.len
            self.cut.Qca = self.cut.nc * self.cut.OExp.wei
            self.cut.Qtot = self.cut.Qca + self.cut.Qba
