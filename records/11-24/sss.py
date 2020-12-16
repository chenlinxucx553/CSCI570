__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/25/2020 8:36 PM'

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# def maxSubArray( nums) -> int:
#     sum = 0
#     maxi = nums[0]
#     for i in range(len(nums)):
#         sum = max(sum + nums[i], nums[i])
#         maxi = max(sum, maxi)
#     return maxi
#
# maxSubArray(nums)

x = -123
str_x = str(x)

if x < 0:
    str_x = str_x[1:]

str_x = str_x[::-1]
print(int(str_x))
