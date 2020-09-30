items = [-1, -3, 7, -3, -17, 0, 18, 12, -44, 8, -12, 4]

idx = []
counter = 2

for i, item in enumerate(items):
    if item > 0 and counter:
        idx.append(i)
        counter -= 1

start, stop = idx[0], idx[-1]

print(sum(items[start + 1:stop]))
