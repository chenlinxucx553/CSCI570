__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/15/2020 11:34 AM'


def split(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = pivot, arr[i + 1]
    return i + 1


def findK(arr, left, right, k):
    if left < right:
        pivot = split(arr, left, right)
        if pivot == k: return arr[pivot]
        if pivot < k:
            return findK(arr, pivot + 1, right, k)
        else:
            return findK(arr, left, pivot - 1, k)


if __name__ == '__main__':
    arr = [2, 1, 4, 3, 5, 9, 8, 0, 1, 3, 2, 5]
    print(findK(arr, 0, len(arr) - 1, 4))
