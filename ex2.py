items = [-1, -3, 7, -3, -17, 0, 18, 12, -44, 8, -12, 4]

idx = []
counter = 2

for i, item in enumerate(items):
    if not counter:
        break

    if item > 0:
        idx.append(i)
        counter -= 1

print(sum(items[idx[0] + 1:idx[-1]]))
