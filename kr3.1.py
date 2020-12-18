import itertools

N = 25
M = 4


items = {
    'marker': 12,
    'pen': 5,
    'pencil': 2
}

goods = {}

for group in itertools.product(items.keys(), repeat=M):
    group_sum = sum([items[item] for item in group])

    if group_sum <= N:
        goods[tuple(sorted(group))] = group_sum

for good, price in goods.items():
    print(repr(good) + ' : ' + str(price))
