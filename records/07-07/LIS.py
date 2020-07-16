__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/7/2020 10:42 AM'

if __name__ == '__main__':
    arr = [1, 5, 3, 4, 6, 9, 7, 8]
    f = [1] * len(arr)

    for x in range(len(arr)):
        for p in range(x):
            if arr[p] < arr[x]:
                f[x] = max(f[x], f[p] + 1)
        print("f[{}] = {}".format(x, f[x]))



    print(max(f))
