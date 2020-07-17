__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/16/2020 4:51 PM'


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            dp = dict()
            max_len = 1
            start = 0
            for j in range(1, len(s)):
                for i in range(0, j):
                    if s[i] == s[j]:
                        if j - i < 3:
                            dp[(i, j)] = True
                        else:
                            dp[(i, j)] = dp[(i + 1, j - 1)]
                    else:
                        dp[(i, j)] = False

                    if dp.get((i, j)):
                        temp_len = j - i + 1
                        if max_len < temp_len:
                            max_len = temp_len
                            start = i

            return s[start: start + max_len]
        else:
            return s


if __name__ == '__main__':
    res = Solution().longestPalindrome("babad")
    print(res)
