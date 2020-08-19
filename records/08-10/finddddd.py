__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/10/2020 3:44 PM'


class Solution:

    def match(self, string, dictionary):
        target = string[0]
        candidate = []
        for word in dictionary:
            if word.startswith(target):
                candidate.append(word)

        indexs = []
        for word in candidate:
            m = len(word)
            if string[:m] == word:
                indexs.append(m)

        return indexs

    def wordBreak(self, s: str, wordDict) -> bool:
        if not s: return True

        temp = [s]
        while temp:
            string = temp.pop()
            indexs = self.match(string, wordDict)
            if len(indexs):
                for index in indexs:
                    temp.append(s[index:])
            else:
                return False

        return True

    def wordBreak2(self, s: str, wordDict) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]


if __name__ == '__main__':
    s = "cars"
    wordDict = ["car", "ca", "rs"]
    Solution().wordBreak2(s, wordDict)
