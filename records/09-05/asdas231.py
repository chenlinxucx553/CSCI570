__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/5/2020 3:58 PM'

weights = [3, 2, 6, 7, 1, 4, 9, 5]  # weight of each item
values = [6, 3, 5, 8, 3, 1, 6, 9]  # value of each item
capacity = 15  # capacity of backpack


def zero_one_bp():
    dummy_capacity = capacity + 1
    dp = [0] * dummy_capacity

    for weight, value in zip(weights, values):
        for cur_capacity in reversed(range(weight, dummy_capacity)):
            # add or not
            dp[cur_capacity] = max(dp[cur_capacity], dp[cur_capacity - weight] + value)
    print(dp[capacity])


def zero_one_bp2():
    dummy_capacity = capacity + 1
    dp = [[0] * dummy_capacity for _ in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for cur_capacity in range(1, dummy_capacity):
            if weights[i - 1] <= cur_capacity:
                dp[i][cur_capacity] = max(dp[i - 1][cur_capacity],
                                          dp[i - 1][cur_capacity - weights[i - 1]] + values[i - 1])
            else:
                dp[i][cur_capacity] = dp[i - 1][cur_capacity]

    print(dp[-1][-1])


if __name__ == '__main__':
    zero_one_bp2()
