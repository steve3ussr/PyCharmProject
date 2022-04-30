import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


class IdealBrakingCurve(object):

    def __init__(self, a_str='a'):
        self.x = None
        self.y = None
        self.sym = sym.symbols(a_str)
        self.curveRange = None

    def setCurve(self, coef_a, coef_b, h, l):
        self.x = self.sym * (coef_b - h / l * self.sym)
        self.y = self.sym * (coef_a + h / l * self.sym)
        return self

    def limitCurve(self, pos, neg):
        temp1 = sym.solve(self.x + self.y - pos)
        temp2 = sym.solve(self.x + self.y - neg)
        left = min(temp1, temp2)
        right = max(temp1, temp2)

        self.curveRange = np.linspace(left, right, 100)
        return self

    def getCurve(self, *args):
        self.x = [(lambda t: self.x.subs(self.sym, t))(i[0]) for i in self.curveRange]
        self.y = [(lambda t: self.y.subs(self.sym, t))(i[0]) for i in self.curveRange]
        plt.plot(self.x, self.y, *args)

