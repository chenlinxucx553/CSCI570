__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/15/2020 11:20 AM'

if __name__ == '__main__':
    arr = [2, 1, 4, 3, 5, 9, 8, 0, 1, 3, 2, 5]
    k = 3
    for i in range(len(arr)):
        pre_idx = i - 1
        current = arr[i]

        while pre_idx >= 0 and arr[pre_idx] > current:
            arr[pre_idx + 1] = arr[pre_idx]
            pre_idx -= 1
        arr[pre_idx + 1] = current

    print(arr)
