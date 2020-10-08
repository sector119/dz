items = []

print('Введіть елементи масиву типу int:')

while True:
    try:
        item = int(input('-> '))
    except ValueError:
        print('Елемент не є числом, повторіть введення ', end='')
        continue
    except KeyboardInterrupt:
        break

    items.append(item)

print(max(items, key=abs))
