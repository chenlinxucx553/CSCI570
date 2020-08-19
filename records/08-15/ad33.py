__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/15/2020 11:52 AM'


class Solution:
    def smallestK(self, arr, k: int):

        from collections import deque

        def insert(array, num):
            index = 0
            for i, val in enumerate(array):
                if val > num:
                    index = i
                    break

            for i in range(len(array) - 1, index, -1):
                array[i] = array[i - 1]

            array[index] = num
            return array

        if not arr: return []
        if k == 1: return [min(arr)]

        res = deque(maxlen=k)
        res.extend(arr[:k])
        sorted(res)
        for val in arr[k:]:
            if val > res[-1]:
                continue
            else:
                res[-1] = float('inf')
                res = insert(res, val)

        return list(res)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4

    res = Solution().smallestK(arr, k)
    print(res)
