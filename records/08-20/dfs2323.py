__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/20/2020 6:10 PM'


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        target = sum(stones) / 2.0
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                if x + y <= target:
                    addition.add(x + y)
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


if __name__ == '__main__':
    arr = [2, 7, 4, 1, 8, 1]
    res = Solution().lastStoneWeightII(arr)
    print(res)
