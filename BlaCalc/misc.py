import math


class Exp:
    def __init__(self, p: float, w: float, l: float, Ic: float, name: str):
        self.phi = p
        self.wei = w
        self.len = l
        self.Ic = Ic
        self.__name__ = name

# (Φ32mm x 0.4kg x 420mm)
# (Φ32mm x 0.25kg x 295mm)
# (Φ17mm x 0.1kg x 500mm)


mm_exp = Exp(32, 0.4, 0.42, 0.95, 'MegaMex')
em_exp = Exp(32, 0.25, 0.295, 0.85, 'Emulsion')
nf_exp = Exp(17, 0.1, 0.5, 0.25, 'NewFinex')


class Cut:
    def __init__(self):
        self.A: float = 0  # drill length for advance for V-Cut, not sure we need it or not yet
        self.H: float = 0  # drill length actual
        self.H2: float = 0  # 2nd row drill length actual for V-Cut
        self.H3: float = 0  # 3rd row drill length actual for V-Cut
        self.B: float = 0  # burden
        self.B2: float = 0  # secondary burden for V-Cut
        self.S: float = 0  # spacing
        self.h0: float = 0  # stemming length
        self.hb: float = 0  # bottom charging length
        self.Ic: float = 0  # column charge concentration
        self.Ib: float = 0  # bottom charge concentration
        self.Qc: float = 0  # column explosive weight theory
        self.Qb: float = 0  # bottom explosive weight theory
        self.Qca: float = 0  # column explosive weight applied
        self.Qba: float = 0  # bottom explosive weight applied
        self.Qtot: float = 0  # total explosive weight applied
        self.nc: float = 0  # column explosive number of catridge
        self.nb: float = 0  # bottom explosive number of catridge
        self.L: float = 0  # Total length of charged hole
        self.W: float = 0  # width of the square
        self.Dia: float = 0
        self.N: int = 0
        self.OExp = mm_exp
        self.IExp = nf_exp

    def summary(self):
        print(f'self.A : {self.A}')
        print(f'self.H : {self.H}')
        print(f'self.H2 : {self.H2}')
        print(f'self.H3 : {self.H3}')
        print(f'self.B : {self.B}')
        print(f'self.B2 : {self.B2}')
        print(f'self.S : {self.S}')
        print(f'self.h0 : {self.h0}')
        print(f'self.hb : {self.hb}')
        print(f'self.Ic : {self.Ic}')
        print(f'self.Ib : {self.Ib}')
        print(f'self.Qc : {self.Qc}')
        print(f'self.Qb : {self.Qb}')
        print(f'self.Qca : {self.Qca}')
        print(f'self.Qba : {self.Qba}')
        print(f'self.nc : {self.nc}')
        print(f'self.nb : {self.nb}')
        print(f'self.Qtot : {self.Qtot}')
        print(f'self.L : {self.L}')
        print(f'self.W : {self.W}')
        print(f'self.Dia : {self.Dia}')
        print(f'self.N : {self.N}')
        print(f'self.OExp : {self.OExp}')
        print(f'self.IExp : {self.IExp}')


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


class OutCut:
    def __init__(self):
        self.cut = Cut()
        self.__name__ = 'Out-Cut'  # abstract class

    def set_param(self, param):
        self.cut.A = param['A']
        self.cut.H = param['H']
        if 'Dia' in param.keys() and 'n' in param.keys():
            self.cut.Dia = param['Dia']
            self.cut.N = param['n']
        self.cut.IExp = param['IExp']
        self.cut.OExp = param['OExp']

    @property
    def name(self):
        print(f'my name is cent cut, abstract')
        return self.__name__

    @name.setter
    def name(self, name: str):
        self.__name__ = name

    def print_summary(self):
        print(f'------ {self.name} ------------')
        self.cut.summary()
        print('------------------')


def rnd(v: float, d: float = 0):
    v2 = v * 2 * math.pow(10, d)+0.5
    n = round(v2)
    return n / 2 / math.pow(10, d)
