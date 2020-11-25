import time


def show_train(train):
    print(f"Number: {train['number']}")
    print(f"Destination: {train['destination']}")
    print(f"Departure time: {time.strftime('%H:%M', train['departure_time'])}")


n = 3
trains = []

while n:
    t_number = input('Enter train number: ')
    t_destination = input('Enter train destination: ')
    t_departure_time = input('Enter train departure time at H:M format: ')

    train = {
        'number': int(t_number),
        'destination': t_destination,
        'departure_time': time.strptime(t_departure_time, '%H:%M')
    }

    trains.append(train)

    n -= 1

trains.sort(key=lambda t: t['number'])

for train in trains:
    show_train(train)

number = int(input('Enter train number to show: '))

for train in trains:
    if train['number'] == number:
        show_train(train)
        break
else:
    print('Train not found')
