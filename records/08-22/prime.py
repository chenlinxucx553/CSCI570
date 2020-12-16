__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/22/2020 9:45 PM'


def find_all_prime(num):
    res = []
    for val in range(2, num + 1):
        prime = True
        for y in range(2, val):
            if val % y == 0:
                prime = False
        if prime:
            res.append(val)

    return res


res = find_all_prime(40)
print(res)
