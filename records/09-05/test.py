__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/5/2020 3:27 AM'


class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        min_val = min([a, b, c])
        rest = list(map(lambda val: val - min_val, [a, b, c]))
        rest.sort()
        new_a, new_b = rest[1], rest[2]

        min_temp = new_a // 2
        new_a -= min_temp
        new_b -= min_temp
        min_val += min_temp

        max_comb = 0
        new_c = 0
        while new_a > 0 and new_b > 0:
            new_a -= 1
            new_b -= 1
            new_c += 1
            temp_max = max_comb
            max_comb = min([new_a, new_b, new_c])
            if temp_max <= max_comb:
                continue
            else:
                break

        single_comb = 0
        if new_a >= 2 or new_b >= 2:
            single_comb = new_a if new_a else new_b
            if single_comb > 5:
                single_comb //= 5


        return min_val + max_comb + single_comb


if __name__ == '__main__':
    res = Solution().numberofprize(9, 3, 3)
    print(res)
