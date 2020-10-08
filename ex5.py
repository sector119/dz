import functools


@functools.lru_cache(maxsize=100)
def xi(i):
    if i <= 3:
        return 1.0

    return xi(i - 1) + xi(i - 3)


def main():
    s = 0
    start = 1
    stop = 100

    for i in range(start, stop + 1):
        s += xi(i) / (2 ** i)

    print(s)


main()
