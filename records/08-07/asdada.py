__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 3:08 PM'


class Solution:
    def kClosest(self, points, K: int):
        if not points: return []

        distance = list(map(lambda item: (item[0], item[1][0] ** 2 + item[1][1] ** 2), enumerate(points)))

        distance.sort(key=lambda item: item[1])

        res = []
        for i in range(K):
            index = distance[i][0]
            res.append(points[index])

        return res


if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    ss = Solution().kClosest(points, K)
    print(ss)
