__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/16/2020 5:06 PM'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 1:
            max_len = 1
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    # temp_str = s[i: j]
                    if len(set(s[i:j])) == j - i:
                        max_len = max(j - i, max_len)
                    else:
                        break
            return max_len
        else:
            return len(s)


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("abcabcbb")
    print(res)
