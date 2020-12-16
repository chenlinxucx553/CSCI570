__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/4/2020 11:43 PM'

#
#
# class Solution:
#     def change(self, amount: int, coins) -> int:
#         dp = [[1] + [0] * amount] * (len(coins) + 1)
#         for c in range(1, len(coins) + 1):
#             for k in range(1, amount + 1):
#                 if k - coins[c - 1] >= 0:
#                     dp[c][k] = dp[c - 1][k] + dp[c][k - coins[c - 1]]
#                 else:
#                     dp[c][k] = dp[c - 1][k]
#         return dp[-1][-1]
#
#
# coins = [1, 2, 5]
#
# Solution().change(5, coins)


# try:
#     number = int(input("请输入数字："))
#     print("number:", number)
#     print("=======hello======")
# except Exception as e:
#     # 报错错误日志
#     print("打印异常详情信息： ", e)
# else:
#     print("没有异常")
# finally:
#     print("finally")
# print("end")


# z = 12.34 + 34j
# print(z.imag)
from sys import argv

asd = {1: 2, 3: 4}
# for item in asd.keys():
#     print(type(item))
print(asd.items())

# def func(*args):
#     print(args)
#
# if __name__ == '__main__':
#     print(argv)
#     s = '1'
#     func(s)
x = 3
y = 8
min = x if x < y else y
print(min)


sss = 'asdsa"ass'

yuan = (1,'a',['a'])

print(yuan)