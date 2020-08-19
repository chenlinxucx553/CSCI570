__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/14/2020 8:21 PM'

class Solution:
    def longestCommonPrefix(self, strs) -> str:

        res = []
        for item in zip(*strs):
            combinations = list(item)
            if all(list(map(lambda val: val == combinations[0], combinations))):
                res.append(combinations[0])
            else:
                break

        return "".join(res)


if __name__ == '__main__':
    arr = ["flower","flow","flight"]
    res = Solution().longestCommonPrefix(arr)
    print(res)