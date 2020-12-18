import math


class Rational:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)

        sign = denominator / abs(denominator)

        self.numerator = int(sign * numerator / gcd)
        if numerator == 0:
            self.denominator = 1
        else:
            self.denominator = int(sign * denominator / gcd)

    def __eq__(self, other):
        same_numerator = self.numerator == other.numerator
        same_denominator = self.denominator == other.denominator
        return same_numerator and same_denominator

    def __gt__(self, other):
        same_numerator = self.numerator > other.numerator
        same_denominator = self.denominator < other.denominator
        return same_numerator and same_denominator

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        return Rational(
            self.numerator * other.denominator +
            other.numerator * self.denominator,
            self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(
            self.numerator * other.denominator -
            other.numerator * self.denominator,
            self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator)


rational_number_list = [
    Rational(1, 5),
    Rational(1, 6),
    Rational(1, 8),
    Rational(2, 5),
    Rational(1, 3),
    Rational(1, 4)
]

print(sorted(rational_number_list, reverse=True))

x = Rational(1, 2)

for i in range(len(rational_number_list)):
    if i % 2 == 0:  # even
        rational_number_list[i] *= x
    else:
        rational_number_list[i] /= x

print(rational_number_list)

print('Sum:', sum(rational_number_list[2:-1], rational_number_list[1]))
