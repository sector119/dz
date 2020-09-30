n = int(input('Введіть к-ть елементів масиву: '))

items = []

while n != 0:
    item = input('-> ')

    while not item.lstrip('-').isdigit():
        item = input('Елемент не є числом, повторіть введення -> ')

    items.append(int(item))
    n -= 1

print(max(items, key=abs))
