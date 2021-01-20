__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/18/2020 3:53 PM'


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')[::-1]
        words = list(filter(lambda item: item != '', words))
        return " ".join(words)

    def nthUglyNumber(self, n: int) -> int:

        res = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        num = 12
        while True:
            if len(res) >= n:
                break

            num += 1

            div_a, res_a = divmod(num, 2)
            div_b, res_b = divmod(num, 3)
            div_c, res_c = divmod(num, 5)

            if res_a == 0 and div_a in res:
                res.append(num)
                continue
            if res_b == 0 and div_b in res:
                res.append(num)
                continue
            if res_c == 0 and div_c in res:
                res.append(num)
                continue

            # if res_a in res or res_b in res or res_c in res:
            #     res.append(num)
            #     continue

        return res[n - 1]


# Solution().reverseWords("a good   example")

Solution().nthUglyNumber(15)