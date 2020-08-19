__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/10/2020 9:33 PM'


class Solution:

    def __init__(self):
        self.count = 0

    def isHappy(self, n: int) -> bool:
        self.count += 1
        val = sum([int(c) ** 2 for c in list(str(n))])

        if self.count > 100:
            return False

        if val != 1:
            return self.isHappy(val)
        else:
            return True
