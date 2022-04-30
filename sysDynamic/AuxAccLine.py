import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


class AuxAccLine(object):

    def __init__(self):
        self.x = None
        self.y = None
        self.curveRange = None

    def setCurve(self, num1, num2):
        minNum = min(num1, num2)
        maxNum = max(num1, num2)
        temp = minNum + maxNum
        self.x = np.linspace(minNum, maxNum, 100)
        self.y = temp - self.x
        return self

    def getCurve(self, *args):
        plt.plot(self.x, self.y, color='k', linewidth=0.5)
