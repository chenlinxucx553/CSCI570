__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 4:48 AM'


def gen_prime(num):
    res = set()
    for val in range(1, num + 1):
        if val > 1:
            for i in range(2, val):
                if val % i == 0:
                    break
        else:
            res.add(val)
    return sorted(list(res))


def go_find_sum(candidate, num):
    # i, j = 0, len(candidate) - 1

    res = []
    for i in range(0, len(candidate)):
        j = i
        while j <= len(candidate):
            if sum(candidate[i:j]) == num:
                res.append((i, j))
                break
            elif sum(candidate[i:j]) > num:
                break
            j += 1

    print(res)
    return len(res)


while True:
    try:

        num = int(input().split()[0])
        candidate = gen_prime(num)

        print(go_find_sum(candidate, num))

    except:
        break
