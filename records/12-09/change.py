__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/9/2020 10:22 AM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        # return res

    return wrapper


class Solution:
    @show
    def lemonadeChange(self, bills) -> bool:

        if not bills:
            return True

        if bills[0] != 5:
            return False

        casher = {
            5: 1,
            10: 0,
            20: 0
        }

        for val in bills[1:]:
            if val == 5:
                casher[5] += 1
            elif val == 10:
                casher[10] += 1
                num_change_5 = casher.get(5)
                if num_change_5 < 1:
                    return False
                else:
                    casher[5] -= 1
            elif val == 20:
                casher[20] += 1
                num_change_5 = casher.get(5)
                num_change_10 = casher.get(10)
                if num_change_5 > 3:
                    casher[5] -= 3
                    continue
                if num_change_5 >= 1 and num_change_10 >= 1:
                    casher[5] -= 1
                    casher[10] -= 1
                    continue
                else:
                    return False

        return True


bills = [10, 5, 5, 5, 5, 5, 20, 5, 5, 20, 20, 5, 20, 5, 20, 20, 5, 20, 20, 5]
Solution().lemonadeChange(bills)
