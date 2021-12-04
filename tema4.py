from math import gcd


class Fraction():

    def __init__(self, top, bottom):
        self.num = top
        self.denom = bottom

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        new_num = self.num * other.denom + self.denom * other.num
        new_denom = self.denom * other.denom
        common_divisor = gcd(new_num, new_denom)
        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def __sub__(self, other):
        new_num = self.num * other.denom - self.denom * other.num
        new_denom = self.denom * other.denom
        common_divisor = gcd(new_num, new_denom)

        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def __invert__(self):
        return f"{self.denom}/{self.num}"


my_fraction = Fraction(5, 2)
my_fraction2 = Fraction(3, 4)
print(my_fraction + my_fraction2)
print(my_fraction - my_fraction2)
print(my_fraction2.__invert__())