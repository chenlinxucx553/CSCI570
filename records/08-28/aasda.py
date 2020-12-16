__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/28/2020 10:55 PM'


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        i, j = 0, len(s)
        if_palindrome = lambda item: item == item[::-1]

        while 0 < j:
            if if_palindrome(s[i: j]):
                break
            else:
                j -= 1

        pre = []
        if j == 0:
            pre = list(s[::-1])
        else:
            pre = list(s[j:])[::-1]

        pre.extend(list(s))
        return "".join(pre)


if __name__ == '__main__':
    ss = "abcd"
    res = Solution().shortestPalindrome(ss)
    print(res)
