__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 4:10 PM'


class Solution:
    def generateParenthesis(self, n: int) -> list:

        res = []
        if n == 0: return res

        def backtrace(result, left, right):
            if left == 0 and right == 0:
                res.append(result)
                return
            if left > 0:
                backtrace(result + "(", left - 1, right)

            if right > left:
                backtrace(result + ")", left, right - 1)

        backtrace("", n, n)

        return res



if __name__ == '__main__':
    Solution().generateParenthesis(3)
    print(5 // 2)