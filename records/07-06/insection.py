__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/6/2020 8:30 PM'

if __name__ == '__main__':
    arr = [32, 5, 6, 3, 123, 5, 8, 54, 45, 6, 77, 7, 5, 5, 56, 5, 5, 233]
    for i in range(len(arr)):
        prev_idx = i - 1
        current = arr[i]
        while prev_idx >= 0 and arr[prev_idx] < current:
            arr[prev_idx + 1] = arr[prev_idx]
            prev_idx -= 1
        arr[prev_idx + 1] = current


    print(arr)

