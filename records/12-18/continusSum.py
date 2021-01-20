__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/18/2020 3:30 PM'


class Solution:
    def findContinuousSequence(self, target: int):
        if target < 3:
            return []
        else:
            res = []
            nums = list(range(1, target))
            left, right = 0, len(nums)
            while left < len(nums) - 1:
                for offset in range(2, len(nums) - left):
                    if sum(nums[left: left + offset]) == target:
                        res.append(nums[left: left + offset])
                    elif sum(nums[left: left + offset]) > target:
                        break
                left += 1

            return sorted(res, key=lambda vals: vals[0])


res = Solution().findContinuousSequence(9)

print(res)
