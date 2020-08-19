__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/14/2020 3:28 PM'


class Solution:
    def reverse(self, x: int) -> int:

        flag = True
        i = 0
        x_str = list(str(x))
        if x < 0:
            flag = False
            x_str = x_str[1:]

        j = len(x_str) - 1

        while i < j:
            x_str[i], x_str[j] = x_str[j], x_str[i]
            i += 1
            j -= 1

        k = 0
        for val in x_str:

            if val == '0':
                k += 1
            else:
                break

        row_data = ''.join(x_str[k:])
        if len(row_data) > 0:
            row_num = int(''.join(row_data)) * (1 if flag else -1)
            if -2 ** 31 <= row_num <= 2 ** 31 - 1:
                return row_num
            else:
                return 0
        return 0


if __name__ == '__main__':
    s = 123
    res = Solution().reverse(s)
    print(res)
