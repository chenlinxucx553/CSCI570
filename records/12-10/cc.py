__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/12/2020 8:26 PM'


def combine(n: int, k: int):
    result = []

    def recall(n, k, start, result, subset):
        if len(subset) == k:
            result.append(subset[:])
            return
        for i in range(start, n + 1):
            subset.append(i)
            recall(n, k, i + 1, result, subset)
            subset.pop()

    recall(n, k, 1, result, [])
    return result


res = combine(5, 3)
print(res)

ss = [1, 2, 3]
aa = list(map(str, ss))
print(int(''.join(aa)))
