__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/15/2020 4:29 PM'


class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:

        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        self.res = set()
        for index, val in enumerate(nums):
            if val > target:
                break
            L = index + 1
            R = len(nums) - 1
            while L < R:
                if val + nums[L] + nums[R] < target:
                    self.res.add((index, L, R))
                    if L + 1 < R and val + nums[L + 1] + nums[R] < target:
                        self.res.add((index, L + 1, R))
                        L += 1
                    elif L < R - 1 and val + nums[L] + nums[R - 1] < target:
                        self.res.add((index, L, R - 1))
                        R -= 1
                else:
                    R -= 1
        return len(self.res)


if __name__ == '__main__':
    arr = [-2, 0, 1, 3]
    target = 2
    res = Solution().threeSumSmaller(arr, target)
    print(res)
