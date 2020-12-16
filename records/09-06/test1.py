__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2020 4:51 AM'


def find_indexs(list_data, target):
    res = []
    for idx, val in enumerate(list_data):
        if val == target:
            res.append(idx)
    return res


def maxmize_sub_aceding_arr(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    ans = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])
    return ans


while True:
    try:
        T = int(input().split()[0])
        data = []
        res = []
        for _ in range(T):
            n = int(input().split()[0])
            data.append(list(map(int, input().split())))

        for arr in data:
            sorted_arr = sorted(arr)
            temp_res = []
            index_dict = {}
            for val in sorted_arr:
                if val not in index_dict:
                    indexs = find_indexs(arr, val)
                    index_dict[val] = indexs
                    if len(indexs) == 1:
                        continue
                    left, right = indexs[0], indexs[-1]
                    if temp_res and left + len(arr) - right < max(temp_res):
                        continue
                    max_left = maxmize_sub_aceding_arr(arr[:left][::-1])
                    max_right = maxmize_sub_aceding_arr(arr[right + 1:])
                    temp_res.append(2 * min(max_left, max_right) + 2)
            if not temp_res:
                res.append('0')
            else:
                res.append(str(max(temp_res)))

        print("\n".join(res))

    except:
        break
