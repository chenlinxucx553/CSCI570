__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/14/2020 5:12 PM'


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle: return 0

        if haystack == needle: return 0

        i, j = 0, 0
        while i + len(needle) <= len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                i += 1

        return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "pi"

    res = Solution().strStr(haystack, needle)
    print(res)

