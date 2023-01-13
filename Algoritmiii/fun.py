import matplotlib.pyplot as plt
from math import sin, cos
import matplotlib as mpl

x = list(range(-200, 200))
fx = [ (((-1) * 12 * i ** (4 * sin(cos(i)))) - (18 * i ** 3) + (5 * i ** 2) + (10 * i) - 30) for i in x]


mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '-.' #'--'
mpl.rcParams['lines.color'] = 'C0'

plt.axes(facecolor='white')
plt.plot(x,fx)
plt.show()