__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/19/2020 4:39 PM'


class Solution:
    def romanToInt(self, s: str) -> int:

        res = 0
        key_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        pre = None
        for c in s:
            temp = key_map[c]
            if pre and pre < key_map[c]:
                temp -= 2 * pre
            res += temp
            pre = key_map[c]

        print(res)


if __name__ == '__main__':
    Solution().romanToInt("IV")
