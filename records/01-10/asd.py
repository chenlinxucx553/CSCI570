__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '1/10/2021 10:53 PM'


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        chars = list(s)
        pairs.sort(key=lambda item: (item[0], item[1]))
        for pair in pairs:
            a, b = pair[0], pair[1]
            chars[a], chars[b] = chars[b], chars[a]

        return ''.join(chars)


Solution().smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]])
