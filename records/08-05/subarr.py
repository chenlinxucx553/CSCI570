__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/5/2020 4:11 PM'


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        if len(nums) == 0:
            return 0
        d = {0: 1}  # 初始化字典（哈希表），设置-1项的值为0
        pre_sum = 0
        cnt = 0
        for num in nums:
            pre_sum += num
            if d.get(pre_sum - k):
                cnt += d[pre_sum - k]
            if d.get(pre_sum):
                d[pre_sum] += 1
            else:
                d[pre_sum] = 1
        return cnt


arr = [0, 1, 99, -98]
target = 2

Solution().subarraySum(arr, target)