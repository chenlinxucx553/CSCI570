__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/14/2020 10:50 AM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def monotoneIncreasingDigits(self, N: int):

        # if N < 10:
        #     return N
        #
        # i = 0
        # nums = list(map(int, list(str(N))))
        # while i < len(nums) - 1:
        #     if nums[i] <= nums[i + 1]:
        #         i += 1
        #     else:
        #         nums[i] -= 1
        #         # check previous
        #         j = i - 1
        #         while j >= 0:
        #             if nums[j] <= nums[i]:
        #                 j -= 1
        #             else:
        #                 nums[j] -= 1
        #         k = i
        #         while k < len(nums):
        #             nums[k] = 9
        #             k += 1
        #
        # for index in range(len(nums)):
        #     if nums[index] != 0:
        #         break
        #
        # return int(''.join(list(map(str, nums[index:]))))

        s = list(str(N))
        j = None

        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                j = i

        while j < len(s):
            s[j] = '9'
            j += 1

        return int(''.join(s))


Solution().monotoneIncreasingDigits(332)
