import functools
@functools.total_ordering
class RomanNumber(int):
    _roman_number = ''

    def __init__(self, number, system = 10):
            self.number = number
            self.system = system
            self.value = int(self.number, self.system)

    def __str__(self):
        return self.roman

    @property
    def roman(self):
        assert int(1 <= self.value <= 3999), 'Number should be natural in range from 1 to 3999'
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.value // 1000]
        h = hunds[self.value // 100 % 10]
        te = tens[self.value // 10 % 10]
        o = ones[self.value % 10]
        _roman_number = t + h + te + o
        return _roman_number

    def __add__(self, other):
        return RomanNumber(str(self.value + other))

    def __sub__(self, other):
        return RomanNumber(str(self.value - other))

    def __mul__(self, other):
        return RomanNumber(str(self.value * other))

    def __floordiv__(self, other):
        return RomanNumber(str(self.value // other))

    def __eq__(self, other):
        return self.value == other

    def __lt__(self, other):
        return self.value < other


d = RomanNumber('55', 16)
s = RomanNumber('631', 10)
f = RomanNumber('716')

print(s + d)
print(d // 10)
print(s - 10)
print(s)
print(d)
print(s < 650)