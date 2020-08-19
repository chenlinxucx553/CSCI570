__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/11/2020 5:49 PM'

res = set()

def backtrace(nums, temp_res, checked):
    global res
    if len(temp_res) == size:
        temp_res.sort()
        res.add(tuple(temp_res))
        return

    if len(temp_res) > size:
        return

    for i in range(len(nums)):
        if checked[i] == 1:
            continue

        checked[i] = 1
        backtrace(nums, temp_res + [nums[i]], checked)
        checked[i] = 0

def format(arr):
    for pair in arr:
        vals = str(pair)[1:-1].split(',')
        print(''.join(vals))

while True:
    try:
        res.clear()
        n, size = map(int, input().split())

        checked = [0] * n
        nums = [i for i in range(1, n + 1)]

        backtrace(nums, [], checked)
        format(sorted(list(res)))

    except:
        break
