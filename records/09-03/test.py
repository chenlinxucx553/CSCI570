__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/3/2020 7:03 AM'


def get_sub(param1, param2):
    return abs(param1 - param2)


def helper(arr):
    n = len(arr)

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    dp[1][1] = arr[0][0]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            else:
                dp[i][j] = min(get_sub(arr[i - 1][j - 1], dp[i - 1][j]),
                               get_sub(arr[i - 1][j - 1], dp[i + 1][j]),
                               get_sub(arr[i - 1][j - 1], dp[i][j - 1]),
                               get_sub(arr[i - 1][j - 1], dp[i][j + 1]))

    return dp[-1][-1]


while True:
    try:
        n = int(input().split()[0])
        data = []
        for _ in range(n):
            temp = list(map(int, input().split()))
            data.append(temp)

        res = helper(data)
        print(res)

    except:
        break
