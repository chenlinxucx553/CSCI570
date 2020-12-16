__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/3/2020 10:27 PM'


def test(N):
    f0 = 0
    f1 = 1
    distance = 0
    res = 0
    while True:
        f = f0 + f1
        f0 = f1
        f1 = f
        if f <= N:
            distance = N - f
            res = f
        else:
            temp_dis = f - N
            if temp_dis < distance:
                res = f
            break

    print(res)


if __name__ == '__main__':
    # f0 = 0
    # f1 = 1
    # target = 1
    # dis = 0
    # res = 0
    # while True:
    #     f = f0 + f1
    #     f0 = f1
    #     f1 = f
    #     if f < target:
    #         dis = target - f
    #         res = f
    #     else:
    #         if f - target < dis:
    #             res = f
    #         break
    #
    # print(res)
    test(18)
