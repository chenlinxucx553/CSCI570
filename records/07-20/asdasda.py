__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/20/2020 3:59 PM'

import collections


class Solution:
    def findShortestSubArray(self, nums) -> int:
        key_map = collections.defaultdict(list)
        for index, val in enumerate(nums):
            key_map[val].append(index)

        max_len = max(list(map(lambda val: len(val), key_map.values())))

        lens = []
        for values in key_map.values():
            if len(values) == max_len:
                lens.append(values[-1] - values[0] + 1)

        return min(lens)


if __name__ == '__main__':
    arr = [1,2,2,1,2,1,1,1,1,2,2,2]
    res = Solution().findShortestSubArray(arr)
    print(res)