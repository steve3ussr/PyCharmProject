from IdealBrakingCurve import *
from AuxAccLine import *

fig1 = plt.figure(1)
IdealBrakingCurve().setCurve(0.5, 0.5, 520, 2524).limitCurve(1, -1).getCurve('--k')
IdealBrakingCurve().setCurve(0.44, 0.5, 520, 2524).limitCurve(1, -1).getCurve('--r')
IdealBrakingCurve().setCurve(0.4, 0.5, 520, 2524).limitCurve(1, -1).getCurve('c')

i = -1
while i <= 1:
    AuxAccLine().setCurve(0, i).getCurve('k')
    i += 0.2



plt.axis('equal')
plt.xlim(0.6, -1)
plt.ylim(1, -0.6)
plt.xlabel(r"$\frac{F_{UV}}{F_G}$")
plt.ylabel(r"$\frac{F_{UH}}{F_G}$")
plt.title('xxxx')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
