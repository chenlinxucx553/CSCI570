__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/19/2020 4:15 PM'


def find_all_prime(n):
    isPrimes = [1] * n
    res = []
    for i in range(2, n):
        if isPrimes[i] == 1:
            res.append(i)
        else:
            continue
        j = i
        while i * j < n:
            isPrimes[i * j] = 0
            j += 1
    return res


res = find_all_prime(100)
print(res)
