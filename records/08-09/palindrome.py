__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 9:08 PM'


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s: return ""

        is_plalindrome = lambda item: item == item[:: -1]

        ans = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s)+ 1):
                if j - i + 1 > len(ans) and is_plalindrome(s[i:j]):
                    ans = s[i:j]

        return ans


if __name__ == '__main__':
    ss = "bb"
    ans = Solution().longestPalindrome(ss)
    print(ans)
