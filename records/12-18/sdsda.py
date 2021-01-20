__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/18/2020 11:14 AM'


class Solution:
    def printNumbers(self, n: int):
        def dfs(x):
            if x == n:
                res.append(int(''.join(tmp)))
                return

            for i in range(10):
                tmp[x] = str(i)
                dfs(x + 1)

        res = []
        tmp = ['0'] * n
        dfs(0)
        return res[1:]


Solution().printNumbers(2)

ss = ['0', '1']
print(int(''.join(ss)))