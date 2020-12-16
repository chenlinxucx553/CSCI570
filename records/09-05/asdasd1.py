__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/5/2020 4:22 AM'


class Solution:
    def find_best_cut(self, arr):
        arr.sort()
        mid_ids = len(arr) // 2
        init_sum = self.get_var(arr[:mid_ids]) + self.get_var(arr[mid_ids:])
        res = mid_ids
        left = right = mid_ids
        while right < len(arr):
            right += 1
            temp_sum = self.get_var(arr[:right]) + self.get_var(arr[right:])
            if temp_sum > init_sum:
                break
            else:
                init_sum = temp_sum
                res = right

        while left > 0:
            left -= 1
            temp_sum = self.get_var(arr[:left]) + self.get_var(arr[left:])
            if temp_sum > init_sum:
                break
            else:
                init_sum = temp_sum
                res = left

        return res

    def find_best_cut2(self, arr):
        left_vals = self.get_sub_var_list(arr[:])
        right_vals = self.get_sub_var_list(arr[::-1])[::-1]
        min_var = float('inf')
        index = 0
        for idx, right in enumerate(right_vals[1:]):
            if left_vals[idx] + right < min_var:
                min_var = left_vals[idx] + right
                index = idx
        return index + 1



    def get_sub_var_list(self, arr):
        res = []
        temp_sum = 0
        temp_square_sum = 0
        for i in range(len(arr)):
            temp_sum += arr[i]
            temp_square_sum += arr[i] ** 2
            res.append((temp_square_sum / (i + 1)) - (temp_sum / (i + 1)) ** 2)
        return res

    def get_var(self, arr):
        n = len(arr)
        avg = sum(arr) / n
        return sum(map(lambda val: (val - avg) ** 2, arr)) / n


if __name__ == '__main__':
    res = Solution().find_best_cut2([1, 1, 1, 3, 3, 3])
    print(res)
