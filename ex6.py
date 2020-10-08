from itertools import zip_longest
from math import atan, log
from statistics import geometric_mean

from numpy import arange
import matplotlib.pyplot as plt


def grouper(n, iterable, padvalue=None):
    return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)


# n = float(input('Введіть n: '))
n = 7

a = 0.5
b = 2.0

h = (b - a) / n

f = 0.3

cols = 2

data = [y for y in [log(x) + atan(x) for x in arange(1, b, h)] if y > f]

print(f'Середнє геометричне: {geometric_mean(data)}')

print('Дані у вигляді таблиці')
for row in grouper(cols, data, ''):
    for col in row:
        print(f'{str(col):>20}', end='')

    print()

plt.plot(data)
plt.ylabel('y')
plt.show()
