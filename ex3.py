items = [0, 1, 2, 0, 0, 3, 0, 0, 4, 5, 0, 6, 0]

# print(items.sort(key=lambda item: item == 0))

for i in range(0, len(items)):
    items.append(items.pop(items.index(0)))

print(items)
