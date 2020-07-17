__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/16/2020 4:01 PM'


class Solution:
    def diffusion(self, str_val, left, right):
        while left >= 0 and right < len(str_val) and str_val[left] == str_val[right]:
            left -= 1
            right += 1
        return str_val[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            res = s[0]
            for i in range(len(s)):
                temp_res = self.diffusion(s, i, i)
                temp_res2 = self.diffusion(s, i, i + 1)
                temp_max = temp_res if len(temp_res) > len(temp_res2) else temp_res2
                if len(res) < len(temp_max):
                    res = temp_max
            return res
        else:
            return s


if __name__ == '__main__':
    res = Solution().longestPalindrome("ac")
    print(res)
