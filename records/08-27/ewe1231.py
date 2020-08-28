__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/27/2020 10:28 PM'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        size = len(s)
        i, j = 0, 1
        max_unique = 0
        while i < size and j < size:
            print(s[i:j])
            if j - i == len(set(s[i:j])):
                j += 1
            else:
                max_unique = max(max_unique, j - i)
                i = j - 1

        return max(max_unique, j - i)


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("ab")
    print(res)
