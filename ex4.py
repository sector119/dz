n = int(input('Введіть к-ть елементів масиву типу int: '))

d = 0
s = 0
f = False

while n != 0:
    n -= 1

    x = int(input('Число: '))

    if x == 0:
        f = True
    elif not f:
        s += x
        d += 1

print(s/d)
