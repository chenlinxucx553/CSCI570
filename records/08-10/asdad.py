__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/10/2020 9:12 PM'


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if not a or not b: return a if a else b

        if len(a) < len(b):
            a, b = b, a

        difference_val = len(a) - len(b)
        while difference_val:
            b = '0' + b
            difference_val -= 1

        carry = 0
        res = []
        for i in range(len(a) - 1, -1, -1):
            sum_val = int(a[i]) + int(b[i]) + carry
            res.append(str(sum_val % 2))
            carry = sum_val // 2

        if carry != 0:
            res.append(str(carry))

        res.reverse()
        return "".join(res)


if __name__ == '__main__':
    a = "11"
    b = "1"
    res = Solution().addBinary(a, b)
    print(res)
