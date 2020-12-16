__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/15/2020 9:45 AM'


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(' ')):
            return False

        words = s.split(' ')
        index = 96
        key_map = {}
        signature = []
        for word in words:
            if word not in key_map:
                index += 1
                key_map[word] = chr(index)
            signature.append(key_map[word])

        return ''.join(signature) == pattern


pattern = "abba"
strs = "dog cat cat dog"
res = Solution().wordPattern(pattern, strs)
print(res)
