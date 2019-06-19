import logging
import functools

logger = logging.getLogger('RomanNumber')


@functools.total_ordering
class RomanNumber():
    logger.debug('started class RomanNumber')
    _roman_number = ''

    def __init__(self, number, system = 10):
        logger.debug(f'takes arguments: {number}, {system}')
        self.number = str(number)
        self.system = system
        self.value = int(self.number, self.system)
        logger.debug(f'self.value takes {self.value}')

    def __str__(self):
        logger.debug(f'__str__ return {self.roman}')
        return self.roman

    @property
    def roman(self):
        logger.debug('def roman start')
        try:
            assert 1 <= self.value <= 3999
        except:
            logger.debug('self.value assertion error')
            return 'Number should be natural in range from 1 to 3999'
        else:
            logger.debug('self.value valid')
            ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            thous = ["", "M", "MM", "MMM", "MMMM"]

            t = thous[self.value // 1000]
            h = hunds[self.value // 100 % 10]
            te = tens[self.value // 10 % 10]
            o = ones[self.value % 10]
            _roman_number = t + h + te + o
            logger.debug(f'def roman return {_roman_number}')
            return _roman_number

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(str(self.value + other.value))
        return RomanNumber(str(self.value + other))

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(str(self.value - other.value))
        return RomanNumber(str(self.value - other))

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(str(self.value * other.value))
        return RomanNumber(str(self.value * other))

    def __truediv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(str(self.value // other.value))
        return RomanNumber(str(self.value // other))

    def __eq__(self, other):
        if isinstance(other, RomanNumber):
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.value < other.value
        return self.value < other


# d = RomanNumber(55)
# s = RomanNumber(631, 16)
# f = RomanNumber('716')
#
# print(s + d)
# print(d / 10)
# print(d - 10)
# print(s)
# print(d)
# print(s < 650)
# print(s > d)