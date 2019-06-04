import functools
@functools.total_ordering
class RomanNumber(int):

    def __init__(self, number, system = 10):
            self.number = number
            self.system = system
            self.value = int(self.number, self.system)
    @property
    def roman(self):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.value // 1000]
        h = hunds[self.value // 100 % 10]
        te = tens[self.value // 10 % 10]
        o = ones[self.value % 10]
        self.number = t + h + te + o
        if self.number:
            return self.number
        else:
            return float('nan')

    def __add__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other


d = RomanNumber('55', 16)
s = RomanNumber('631', 10)
print(s - d)
print(d / 10)
print(s.roman)