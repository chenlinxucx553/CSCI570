__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/6/2020 10:46 AM'

if __name__ == '__main__':
    arr = [73, 56, 91, 47, 82, 49]
    for i in range(3):
        current = arr[i]
        low, high = 0, i - 1
        while low <= high:
            mid = int((low + high) / 2)
            if current < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        arr[low] = current

    print(arr)

