from math import atan, log

from statistics import geometric_mean
from numpy import arange

n = float(input('Введіть n: '))

a = 0.5
b = 2.0

h = (b - a) / n

f = 0.3

data = filter(lambda y: y > f, [log(x) + atan(x) for x in arange(1, b, h)])

print(f'Середнє геометричне: {geometric_mean(data)}')
