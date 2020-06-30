__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/28/2020 5:58 PM'

if __name__ == '__main__':
    info = [(0, 0), (1, 1500), (4, 3000), (3, 2000), (1, 2000)]
    # print(info[:, 1])

    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(list(zip(*a))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# def difference_by(a, b, fn):
#     b = set(map(fn, b))
#     return [item for item in a if fn(item) not in b]
#
#
# from math import floor
# print(difference_by([2.1, 1.2], [2.3, 3.4],floor)) # [1.2]
# difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])


    ss = [item for item in a if len(item) != 2]
    print(ss)
