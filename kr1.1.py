import math


def ak(k):
    if k == 1:
        return 1.0

    return 1 / 2 * (math.sqrt(bk(k - 1)) + 1 / 2 * math.sqrt(ak(k - 1)))


def bk(k):
    if k == 1:
        return 1.0

    return 2 * ak(k - 1) ** 2 + bk(k - 1)


def main():
    k = 5

    print(ak(5))


main()
