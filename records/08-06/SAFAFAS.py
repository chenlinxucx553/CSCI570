__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/6/2020 5:02 AM'


def isPrime(num):
    if num <= 1:
        return False
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def find_huiwen(val):
    candidates = []
    chars = str(val)  # '110'
    isPalindrome = lambda x: x == x[::-1]
    i, j = 0, len(chars) - 1
    patience = 1
    while i < j:
        if chars[i] != chars[j] and patience:
            patience -= 1
            temp1, temp2 = list(chars), list(chars)
            del temp1[i]
            del temp2[j]
            if isPalindrome("".join(temp1)):
                candidates.append(int("".join(temp1)))
            if isPalindrome("".join(temp2)):
                candidates.append(int("".join(temp2)))

        i += 1
        j -= 1
    if patience == 1:
        candidates.append(int(str(chars[:i] + chars[j + 1:])))

    return candidates


while True:
    try:
        n, m = map(int, input().split())

        res = set()
        count = 0
        for val in range(n, m + 1):
            candidates = find_huiwen(val)
            for num in candidates:
                if num in res or isPrime(num):
                    count += 1
                    res.add(num)

        print(count)

    except:
        break
