__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 11:46 PM'


def find_all_prime(num):
    res = set()
    for val in range(2, num + 1):
        prime = True
        for y in range(2, val):
            if val % y == 0:
                prime = False
        if prime:
            res.add(val)

    return res


def is_prime(num):
    if num == 0: return False
    if num == 1: return False

    for y in range(2, num):
        if val % y == 0:
            return False

    return True


if __name__ == "__main__":
    # # 读取第一行的n
    n = int(input().strip())
    values = list(map(int, input().split()))
    ans = 0
    for val in values:
        times = val // 2
        val -= 2 * times
        if is_prime(val):
            ans += 1

        ans += times

    print(ans)
