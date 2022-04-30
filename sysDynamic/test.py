import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

x = sym.symbols('x')
y = x**2 - 2
res = sym.solve(y)
print(y)
print(res)

u = np.linspace(1, 10, 10)
v = 3 - u
print(v)
print("done")



