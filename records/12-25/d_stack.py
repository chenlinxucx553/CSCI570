__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/25/2020 10:17 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
