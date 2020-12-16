__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/10/2020 10:26 AM'

from collections import defaultdict


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def bestLine(self, points):
        # A = Y2 - Y1 B = X1 - X2 C = X2Y1 - X1Y2
        lines = defaultdict(list)
        most = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b, c = self.abc(points[i], points[j])
                g = self.gcd(a, b)
                if a // g > 0:
                    a, b, c = (a // g, b // g, c // g)
                else:
                    a, b, c = (-a // g, -b // g, -c // g)

                sign = tuple((a, b, c))
                lines[sign].append((i, j))
                most = max(most, len(lines[sign]))

        res = []
        for val in lines.values():
            if len(list(val)) == most:
                res.extend(val)

        return list(sorted(res, key=lambda item: (item[0], item[1]))[0])

    def abc(self, p1, p2):
        a = p2[1] - p1[1]
        b = p1[0] - p2[0]
        c = p2[0] * p1[1] - p1[0] * p2[1]
        return a, b, c

    def gcd(self, a, b):
        while a:
            a, b = b % a, a

        return b


points = [[0, 0], [1, 1], [1, 0], [2, 0]]
Solution().bestLine(points)
