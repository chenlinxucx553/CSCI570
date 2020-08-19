__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/10/2020 5:05 PM'


class Solution:
    def reverse(self, x: int) -> int:
        flag = x < 0
        c_list = [c for c in list(str(x))]
        c_list.reverse()
        res = ""
        for i, c in enumerate(c_list):
            if c.isnumeric():
                res += c


        if not flag:
            res = int(res)
        else:
            res = int(res) * -1

        if -2 ** 31 <= res <= 2 **31 + 1:
            return res
        else:
            return 0

if __name__ == '__main__':
    num = 120
    res = Solution().reverse(num)
    print(res)

    print(2 // 2)