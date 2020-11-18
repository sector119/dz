# Задано ціле значення n та послідовність  a(0), a(1), ..., a(n-1) .
# В послідовності знайти ті числа, що є степенями трійки. Визначити довжину найдовшої послідовності таких чисел.


degrees_of_3 = [num for num in [3**deg for deg in range(10)]]


def checking_value(value):
    while not value.isdigit() or int(value) <= 0:
        value = input("Unsuitable. Try one more time: -> ")

    return int(value)


def get_array(n):
    array = []

    while n != 0:
        array.append(checking_value(input("Enter int number: ")))
        n -= 1

    return array


def count_degrees(degrees_of_3, array):
    count = 0
    counts = []

    for e in array:
        if e in degrees_of_3:
            count += 1
        else:
            counts.append(count)
            count = 0

    return counts


def max_in_counts(counts):
    return max(counts)


n = checking_value(input("Enter n: "))
array = get_array(n)
counts = count_degrees(degrees_of_3, array)
print("Довжина найдовшої послідовності чисел що є степенями трійки: ", max_in_counts(counts))
