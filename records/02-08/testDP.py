__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/8/2021 10:17 PM'

if __name__ == '__main__':

    p = 5
    dis = [1, 3, 8, 11, 15, 18, 20, 21]
    intervals = [b - a for a, b in zip(dis[:-1], dis[1:])]
    intervals.insert(0, dis[0])
    print(intervals) # [1, 2, 5, 3, 4, 3, 2, 1]

    remain = p
    dp = [0] * (len(dis) + 1)

    for i in range(1, len(dis) + 1):
        if remain < intervals[i - 1]:
            dp[i] = dp[i - 1] + 1
            remain = p
        else:
            dp[i] = dp[i - 1]
            remain -= intervals[i - 1]

    print(dp[1:])
