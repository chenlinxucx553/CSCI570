__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/3/2020 8:12 AM'


def get_sub(param1, param2):
    return abs(param1 - param2)


def get_val(arr, i, j):
    n = len(arr)
    if 0 <= i < n and 0 <= j < n:
        return arr[i][j]
    else:
        return float('inf')


def get_min(arr, i, j):
    return min(abs(arr[i][j] - get_val(arr, i - 1, j)),
               abs(arr[i][j] - get_val(arr, i, j + 1)),
               abs(arr[i][j] - get_val(arr, i + 1, j)),
               abs(arr[i][j] - get_val(arr, i, j - 1)))


def helper(arr):
    n = len(arr)

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    dp[1][1] = 0

    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         if i == 1 and j == 1:
    #             continue
    #         else:
    #             dp[i][j] = min(get_sub(arr[i - 1][j - 1], get_val(arr, i - 2, j - 1)),
    #                            get_sub(arr[i - 1][j - 1], get_val(arr, i - 1, j - 2)),
    #                            get_sub(arr[i - 1][j - 1], get_val(arr, i, j - 1)),
    #                            get_sub(arr[i - 1][j - 1], get_val(arr, i - 1, j)))
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = get_min(arr, i, j)
    print(temp)

    return dp[-1][-1]


if __name__ == '__main__':

    n = int(input().split()[0])
    data = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)

    res = helper(data)
    # print(res)
