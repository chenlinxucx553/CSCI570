__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/21/2020 12:13 AM'

histogram = [
    [0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0]

]
N = len(histogram)
M = len((histogram[0]))

for j in range(M):
    for i in range(1, N):
        if histogram[i][j] == 1:
            histogram[i][j] += histogram[i - 1][j]  # 构造直方图


# 函数: 计算直方图中的最大矩形
def maxRect(nums):
    stack = []
    maxArea = 0
    nums.append(0)
    for i in range(len(nums)):
        while len(stack) > 0 and nums[stack[-1]] > nums[i]:
            H = nums[stack.pop()]
            sidx = -1
            if len(stack) > 0:
                sidx = stack[-1]
            area = H * (i - sidx - 1)
            maxArea = max(maxArea, area)
        stack.append(i)
    return maxArea


maxR = 0
for i in range(N):
    nums = histogram[i]
    maxR = max(maxR, maxRect(nums))  # 计算每一行 直方图中的最大矩形
print(maxR)
