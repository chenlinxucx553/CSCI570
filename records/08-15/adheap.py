__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/15/2020 12:04 PM'

import heapq


class Solution:
    def smallestK(self, arr, k: int):
        if k > len(arr) or k == 0:
            return []
        heap = []
        for i in arr[:k]:
            heapq.heappush(heap, -i)
        for i in arr[k:]:
            if i < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -i)
        result = []
        for i in range(k):
            result.append(-heapq.heappop(heap))
        return result[::-1]

    def smallestK2(self, arr, k):

        if not arr or k == 0: return []

        if k == 1: return [min(arr)]

        from collections import deque

        res = []

        for index, val in enumerate(arr[k:]):
            res.append((index, val))



if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4

    res = Solution().smallestK2(arr, k)
    print(res)
