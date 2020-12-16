__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/2/2020 9:59 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


@show
def genPrimes(n):
    res = []
    for c in range(2, n):
        for i in res:
            if c % i == 0:
                break
        else:
            res.append(c)
    return res


genPrimes(2)
