__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/26/2021 7:27 PM'

arr = [1, 3, 2, 4, 6, 7, 8, 9, 12, 10, 16, 18, 12, 17, 18, 22, 25, 20, 30]
arr2 = [[2, 1], [4, 3], [1, 2], [5, 4], [7, 6], [200, 100]]


# dp = [0] * len(arr)
#
# dp[-1] = arr[-1]
#
# for i in range(len(arr) - 2, -1, -1):
#     if i + arr[i] < len(arr):
#         dp[i] = max(arr[i] + dp[i + arr[i]], dp[i + 1])
#     else:
#         dp[i] = max(arr[i], dp[i + 1])
#
# print(max(dp))

def get_compound_volume(open_close_pair, volumes):
    result = []
    if len(open_close_pair) == len(volumes):
        # normally, their length should keep the same.
        for index, (o_c, vol) in enumerate(zip(open_close_pair, volumes)):
            open_val, close_val = o_c[0], o_c[1]
            result.append([index, vol, 1 if open_val >= close_val else -1])

        return result


def calculateMA(orginalData, dayCount):
    result = []
    for i in range(0, len(orginalData)):
        if i < dayCount:
            result.append('-')
            continue
        result.append(sum(orginalData[i - 4: i + 1]) / dayCount)

    return result


# ['-', '-', '-', '-', '-', 4.4, 5.4, 6.8, 8.4, 9.2, 11.0, 13.0, 13.6, 14.6, 16.2, 17.4, 18.8, 20.4, 23.0]
result = calculateMA(arr, 10)
print(result)
