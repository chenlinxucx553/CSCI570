__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/21/2020 5:41 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)

    return wrapper


class Solution:
    @show
    def multiply(self, num1: str, num2: str) -> str:

        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = 0
        num2 = list(num2)
        num2.reverse()
        for i, val in enumerate(num2):
            times = 10 ** i
            res += times * int(val) * int(num1)

        return str(res)


class Solution2:
    @show
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        n1 = [int(i) for i in num1]
        n2 = [int(i) for i in num2]
        n1 = n1[::-1]
        n2 = n2[::-1]
        r = []
        rmap = [0 for i in range(len(num1) + len(num2))]
        for i, ni in enumerate(n1):
            for j, nj in enumerate(n2):
                ind = i + j
                rmap[ind] += ni * nj
        while rmap[-1] == 0:
            rmap.pop()
        t = 0
        for x in rmap:
            x += t
            if x >= 10:
                t = x // 10
                x = x % 10
            else:
                t = 0
            r.append(str(x))
        if t > 0:
            r.append(str(t))

        return "".join(r[::-1])

if __name__ == '__main__':
    Solution2().multiply("123", "456")
