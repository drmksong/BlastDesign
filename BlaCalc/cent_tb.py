import math
from plum import dispatch
from charge import *
from misc import *


class CentCut:
    def __init__(self):
        self.W = 0
        self.cut1 = Cut()
        self.cut2 = Cut()
        self.cut3 = Cut()
        self.cut4 = Cut()
        self.cuts = [self.cut1, self.cut2, self.cut3, self.cut4]
        self.__name__ = 'C-Cut'  # abstract class

    def set_param(self, param):

        for cut in self.cuts:
            cut.A = param['A']
            cut.H = param['H']
            if 'H2' in param.keys() and 'H3' in param.keys():
                cut.H2 = param['H2']
                cut.H3 = param['H3']
            if 'B2' in param.keys():
                cut.B2 = param['B2']
            if 'Dia' in param.keys() and 'n' in param.keys():
                cut.Dia = param['Dia']
                cut.N = param['n']

            cut.IExp = param['IExp']
            cut.OExp = param['OExp']

    @property
    def name(self):
        print(f'my name is cent cut, abstract')
        return self.__name__

    @name.setter
    def name(self, name: str):
        self.__name__ = name


class PCut(CentCut):
    def __init__(self):
        super().__init__()
        self.__name__ = 'P-Cut'

    def calc(self):
        self.calc_c1()
        self.calc_c2()
        self.calc_c3()
        self.calc_c4()

    def print_summary(self):
        print(f'------{self.name}------------')
        self.cut1.summary()
        print('------------------')
        self.cut2.summary()
        print('------------------')
        self.cut3.summary()
        print('------------------')
        self.cut4.summary()
        print('------------------')

    def calc_c1(self):
        dia_d = self.cut1.Dia*math.sqrt(3)

        self.cut1.B = 1.5 * dia_d
        self.cut1.h0 = self.cut1.B
        self.cut1.Ic = cc_d(self.cut1.B)
        self.cut1.Qc = self.cut1.Ic*(self.cut1.H - self.cut1.h0)
        self.cut1.Ib = 0
        self.cut1.Qb = 0
        self.cut1.nc = rnd(self.cut1.Qc / (self.cut1.IExp.wei))
        self.cut1.Qca = self.cut1.nc * self.cut1.IExp.wei
        self.cut1.Qba = 0
        self.cut1.Qtot = self.cut1.Qca + self.cut1.Qba
        self.cut1.W = 1.5 * math.sqrt(2) * dia_d
        self.cut1.L = self.cut1.h0 + self.cut1.nc * self.cut1.IExp.len

        if self.cut1.L > self.cut1.H * 1.1:
            n = rnd((self.cut1.L - self.cut1.H)/self.cut1.OExp.len)
            self.cut1.nc = self.cut1.nc - n
            self.cut1.L = self.cut1.h0 + \
                (self.cut1.nb) * self.cut1.IExp.len + \
                (self.cut1.nc) * self.cut1.OExp.len
            self.cut1.Qca = self.cut1.nc * self.cut1.OExp.wei
            self.cut1.Qtot = self.cut1.Qca + self.cut1.Qba

    def calc_c2(self):
        self.cut2.B = self.cut1.W
        self.cut2.h0 = 0.5*self.cut2.B
        self.cut2.Ic = cc_b(self.cut2.B)
        self.cut2.Qc = self.cut2.Ic*(self.cut2.H - self.cut2.h0)
        self.cut2.Ib = 0
        self.cut2.Qb = 0
        self.cut2.nc = rnd(self.cut2.Qc / (self.cut2.IExp.wei))
        self.cut2.Qca = self.cut2.nc * self.cut2.IExp.wei
        self.cut2.Qba = 0
        self.cut2.Qtot = self.cut2.Qca + self.cut2.Qba
        self.cut2.W = 1.5 * math.sqrt(2) * self.cut1.W
        self.cut2.L = self.cut2.h0 + self.cut2.nc * self.cut1.IExp.len

        if self.cut2.L > self.cut2.H * 1.1:
            n = rnd((self.cut2.L - self.cut2.H)/self.cut2.OExp.len)
            self.cut2.nc = self.cut2.nc - n
            self.cut2.L = self.cut2.h0 + \
                (self.cut2.nb) * self.cut2.IExp.len + \
                (self.cut2.nc) * self.cut2.OExp.len
            self.cut2.Qca = self.cut2.nc * self.cut2.OExp.wei
            self.cut2.Qtot = self.cut2.Qca + self.cut2.Qba

        print(f'{self.cut2.L} = {self.cut2.h0} + {self.cut2.nc} * {self.cut1.IExp.len}')

    def calc_c3(self):
        self.cut3.B = min(1, self.cut2.W)
        self.cut3.h0 = 0.5 * self.cut3.B
        self.cut3.Ic = cc_b(self.cut3.B)
        self.cut3.Qc = self.cut3.Ic*(self.cut3.H - self.cut3.h0)
        self.cut3.Ib = 0
        self.cut3.Qb = 0
        self.cut3.nc = rnd(self.cut3.Qc / (self.cut3.IExp.wei))
        self.cut3.Qca = self.cut3.nc * self.cut3.IExp.wei
        self.cut3.Qba = 0
        self.cut3.Qtot = self.cut3.Qca + self.cut3.Qba
        self.cut3.W = 1.5 * math.sqrt(2) * self.cut2.W
        self.cut3.L = self.cut3.h0 + self.cut3.nc * self.cut2.IExp.len

        if self.cut3.L > self.cut3.H * 1.1:
            n = rnd((self.cut3.L - self.cut3.H)/self.cut3.OExp.len)
            self.cut3.nc = self.cut3.nc - n
            self.cut3.L = self.cut3.h0 + \
                (self.cut3.nb) * self.cut3.IExp.len + \
                (self.cut3.nc) * self.cut3.OExp.len
            self.cut3.Qca = self.cut3.nc * self.cut3.OExp.wei
            self.cut3.Qtot = self.cut3.Qca + self.cut3.Qba

    def calc_c4(self):
        self.cut4.B = min(1, self.cut3.W)
        self.cut4.h0 = 0.5 * self.cut4.B

        self.cut4.hb = self.cut4.H / 3
        self.cut4.Ib = cc_b(self.cut4.B)
        self.cut4.Qb = self.cut4.Ib*(self.cut4.hb)

        self.cut4.nb = rnd(self.cut4.Qb / (self.cut4.IExp.wei))
        self.cut4.Qba = self.cut4.nb * self.cut4.IExp.wei

        self.cut4.Ic = self.cut4.Ib / 2
        self.cut4.Qc = self.cut4.Ic*(self.cut4.H - self.cut4.h0 - self.cut4.hb)

        self.cut4.nc = rnd(self.cut4.Qc / (self.cut4.IExp.wei))
        self.cut4.Qca = self.cut4.nc * self.cut4.IExp.wei

        self.cut4.Qtot = self.cut4.Qca + self.cut4.Qba
        self.cut4.W = math.sqrt(2) * (self.cut3.W/2 + min(1, self.cut3.W))
        self.cut4.L = self.cut4.h0 + \
            (self.cut4.nb+self.cut4.nc) * self.cut4.IExp.len

        if self.cut4.L > self.cut4.H * 1.1:
            n = rnd((self.cut4.L - self.cut4.H)/self.cut4.IExp.len)
            self.cut4.nc = self.cut4.nc - n
            self.cut4.L = self.cut4.h0 + \
                (self.cut4.nb) * self.cut4.IExp.len + \
                (self.cut4.nc) * self.cut4.IExp.len
            self.cut4.Qca = self.cut4.nc * self.cut4.IExp.wei
            self.cut4.Qtot = self.cut4.Qca + self.cut4.Qba

        self.W = min(1, self.cut4.W)

    @property
    def name(self):
        print(f'my name is parallel cut, not abstract')
        return self.__name__


class VCut(CentCut):
    def __init__(self):
        super().__init__()
        self.__name__ = 'V-Cut'

    @property
    def name(self):
        print(f'my name is V-cut, not abstract')
        return self.__name__

    def calc(self):
        self.calc_c1()
        self.calc_c2()
        self.calc_c3()

    def print_summary(self):
        print(f'------{self.name}------------')
        self.cut1.summary()
        print('------------------')
        self.cut2.summary()
        print('------------------')
        self.cut3.summary()
        print('------------------')

    def calc_c1(self):

        self.cut1.B = self.cut1.A / 2
        self.cut1.h0 = 0.3 * self.cut1.B
        self.cut1.Ic = cc_b(self.cut1.B)
        self.cut1.Qc = self.cut1.Ic*(self.cut1.H - self.cut1.h0)
        self.cut1.Ib = 0
        self.cut1.Qb = 0
        self.cut1.nc = rnd(self.cut1.Qc / (self.cut1.IExp.wei))
        self.cut1.Qca = self.cut1.nc * self.cut1.IExp.wei
        self.cut1.Qba = 0
        self.cut1.Qtot = self.cut1.Qca + self.cut1.Qba
        self.cut1.L = self.cut1.h0 + self.cut1.nc * self.cut1.IExp.len

        if self.cut1.L > self.cut1.H * 1.1:
            n = rnd((self.cut1.L - self.cut1.H)/self.cut1.IExp.len)
            self.cut1.nc = self.cut1.nc - n
            self.cut1.L = self.cut1.h0 + \
                (self.cut1.nb) * self.cut1.IExp.len + \
                (self.cut1.nc) * self.cut1.IExp.len
            self.cut1.Qca = self.cut1.nc * self.cut1.IExp.wei
            self.cut1.Qtot = self.cut1.Qca + self.cut1.Qba

    def calc_c2(self):
        self.cut2.B = self.cut1.A / 2
        self.cut2.h0 = 0.5*self.cut2.B
        self.cut2.Ic = cc_b(self.cut2.B)
        self.cut2.Qc = self.cut2.Ic*(self.cut2.H2 - self.cut2.h0)
        self.cut2.Ib = 0
        self.cut2.Qb = 0
        self.cut2.nc = rnd(self.cut2.Qc / (self.cut2.IExp.wei))
        self.cut2.Qca = self.cut2.nc * self.cut2.IExp.wei
        self.cut2.Qba = 0
        self.cut2.Qtot = self.cut2.Qca + self.cut2.Qba
        self.cut2.L = self.cut2.h0 + self.cut2.nc * self.cut1.IExp.len

        if self.cut2.L > self.cut2.H2 * 1.1:
            n = rnd((self.cut2.L - self.cut2.H)/self.cut2.IExp.len)
            self.cut2.nc = self.cut2.nc - n
            self.cut2.L = self.cut2.h0 + \
                (self.cut2.nb) * self.cut2.IExp.len + \
                (self.cut2.nc) * self.cut2.IExp.len
            self.cut2.Qca = self.cut2.nc * self.cut2.IExp.wei
            self.cut2.Qtot = self.cut2.Qca + self.cut2.Qba

        print(f'{self.cut2.L} = {self.cut2.h0} + {self.cut2.nc} * {self.cut1.IExp.len}')

    def calc_c3(self):
        self.cut3.B = self.cut3.B2
        self.cut3.h0 = 0.5 * self.cut3.B
        self.cut3.Ic = cc_b(self.cut3.B)
        self.cut3.Qc = self.cut3.Ic*(self.cut3.H3 - self.cut3.h0)
        self.cut3.Ib = 0
        self.cut3.Qb = 0
        self.cut3.nc = rnd(self.cut3.Qc / (self.cut3.IExp.wei))
        self.cut3.Qca = self.cut3.nc * self.cut3.IExp.wei
        self.cut3.Qba = 0
        self.cut3.Qtot = self.cut3.Qca + self.cut3.Qba
        self.cut3.W = 1.5 * math.sqrt(2) * self.cut2.W
        self.cut3.L = self.cut3.h0 + self.cut3.nc * self.cut2.IExp.len

        if self.cut3.L > self.cut3.H3 * 1.1:
            n = rnd((self.cut3.L - self.cut3.H)/self.cut3.IExp.len)
            self.cut3.nc = self.cut3.nc - n
            self.cut3.L = self.cut3.h0 + \
                (self.cut3.nb) * self.cut3.IExp.len + \
                (self.cut3.nc) * self.cut3.IExp.len
            self.cut3.Qca = self.cut3.nc * self.cut3.IExp.wei
            self.cut3.Qtot = self.cut3.Qca + self.cut3.Qba
