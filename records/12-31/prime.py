__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 11:45 AM'


def countPrimes(n):
    # 最小的质数是 2
    if n < 2:
        return 0

    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0

    # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

    return sum(isPrime)


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        for i in range(2, n):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = 0

        return [index for index, num in enumerate(is_prime) if num == 1]


res = Solution().countPrimes(10)
print(res)
