__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/5/2020 3:24 PM'


class Solution:
    def twoSum(self, nums, target: int):

        self.res = []
        self.index = []

        def backtrace(arr, target, visited):
            if target == 0:
                return

            for index, val in enumerate(arr):
                if val in visited:
                    continue

                visited.add(val)
                self.res.append(val)
                self.index.append(index)
                backtrace(arr, target - val, visited)
                visited.remove(val)
                self.res.pop()
                self.index.pop()

        visited = set()

        backtrace(nums, target, visited)
        return self.index


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(arr, target))
