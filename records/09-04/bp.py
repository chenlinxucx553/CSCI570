__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/4/2020 7:13 PM'

# one-zero backpack. process items only once
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


def complete_bp():
    dummy_capacity = capacity + 1
    dp = [0] * dummy_capacity

    for weight, value in zip(weights, values):
        for cur_capacity in range(weight, dummy_capacity):
            dp[cur_capacity] = max(dp[cur_capacity], dp[cur_capacity - weight] + value)
    print(dp[capacity])


if __name__ == '__main__':
    complete_bp()
