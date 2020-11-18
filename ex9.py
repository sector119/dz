n = 3
trains = []

while n:
    t_number = input('Enter train number: ')
    t_destination = input('Enter train destination: ')
    t_departure_time = input('Enter train departure time: ')

    train = {
        'number': int(t_number),
        'destination': t_destination,
        'departure_time': t_departure_time
    }

    trains.append(train)

    n -= 1

trains.sort(key=lambda t: t['number'])

print(trains)

number = int(input('Enter train number to show: '))

for train in trains:
    if train['number'] == number:
        print(train)
        break
else:
    print('Train not found')
