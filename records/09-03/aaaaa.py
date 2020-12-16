__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/3/2020 9:28 AM'


def get_val(arr, i, j):
    n = len(arr)
    if 0 <= i < n and 0 <= j < n:
        return arr[i][j]
    else:
        return float('inf')


def get_4_direction(arr, row, col):
    n = len(arr)
    res = []
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        temp_row = row + i
        temp_col = col + j
        if 0 <= temp_row < n and 0 <= temp_col < n:
            res.append(arr[temp_row][temp_col])
        else:
            res.append(float('inf'))
    return res


def helper(arr):
    n = len(arr)

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            else:
                four_dp = get_4_direction(dp, i, j)
                center = arr[i - 1][j - 1]
                four_dis = list(map(lambda val: abs(val - center), get_4_direction(arr, i - 1, j - 1)))
                dp[i][j] = min(list(map(lambda val: val[0] + val[1], zip(four_dp, four_dis))))
    return dp[-1][-1]


if __name__ == '__main__':
    n = int(input().split()[0])
    data = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)

    res = helper(data)
    print(res)
