__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/14/2020 6:00 PM'


class Solution:

    def __init__(self):
        self.data = ['1', '11', '21', '1211', '111221']

    def read(self, string):
        pre = string[0]
        count = 1
        res = []
        for val in string[1:]:
            if val == pre:
                count += 1
            else:
                res.append(str(count))
                count = 1
                res.append(pre)
                pre = val

        res.append(str(count))
        res.append(pre)
        return "".join(res)

    def countAndSay(self, n: int) -> str:

        if n <= len(self.data):
            return self.data[n - 1]
        else:
            for index in range(5, n):
                self.data.append(self.read(self.data[index - 1]))

            return self.data[-1]


if __name__ == '__main__':
    res = Solution().countAndSay(6)
    print(res)
