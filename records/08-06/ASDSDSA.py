__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/6/2020 4:39 AM'

while True:
    try:
        n = int(input().split()[0])
        part_a = "".join(input().split())
        part_b = "".join(input().split())

        ans = 0
        dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if part_a[i - 1] == part_b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        similarity = round(ans / n, 2)
        if similarity >= 0.50:
            print("{} No".format(similarity))
        else:
            print("{} Yes".format(similarity))

    except:
        break
