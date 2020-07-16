__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/8/2020 9:15 AM'


def heapify(arr, size, root_idx):
    largest_idx = root_idx
    left_node_idx = root_idx * 2 + 1
    right_node_idx = 2 * root_idx + 2
    if left_node_idx < size and arr[largest_idx] < arr[left_node_idx]:
        largest_idx = left_node_idx
    if right_node_idx < size and arr[largest_idx] < arr[right_node_idx]:
        largest_idx = right_node_idx
    if largest_idx != root_idx:
        arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx]
        heapify(arr, size, largest_idx)


def heap_sort(arr):
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
    print(l)
