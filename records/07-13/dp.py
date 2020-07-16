__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/13/2020 12:08 PM'


def func(nums):
    max_val = nums[0]

    for i in range(len(nums)):
        temp = 1
        for j in range(i, len(nums)):
            temp *= nums[j]
            max_val = max(temp, max_val)

    return max_val


if __name__ == '__main__':
    nums = [-2, 0, -1]

    func(nums)
    print("{:,}".format(10241024))
