__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/21/2020 5:37 PM'

from collections import Counter, defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        kv = defaultdict(list)
        for i, c in enumerate(s):
            kv[c].append(i)
        min_k, min_v = None, len(s)
        for k, v in kv.items():
            if len(v) == 1 and min_v > v[0]:
                min_v = v[0]

        return min_v


res = Solution().firstUniqChar("loveleetcode")
print(res)
