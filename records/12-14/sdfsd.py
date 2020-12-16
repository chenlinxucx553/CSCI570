__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/14/2020 11:58 AM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def addStrings(self, num1: str, num2: str):
        i, j = len(num1) - 1, len(num2) - 1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            a, b = int(num1[i]), int(num2[j])
            res.insert(0, str((a + b + carry) % 10))
            carry = (a + b + carry) // 10
            i -= 1
            j -= 1

        left = []
        if i >= 0:
            left = num1[:i + 1]
        elif j >= 0:
            left = num2[:j + 1]

        for index in range(len(left) - 1, -1, -1):
            res.insert(0, str((int(left[index]) + carry) % 10))
            carry = (int(left[index]) + carry) // 10

        if carry:
            res.insert(0, str(carry))

        return ''.join(res)


Solution().addStrings("1", "9")



