__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/23/2020 11:23 AM'

from heapq import heapify, heappush, heappop
from itertools import count

"""
https://www.cnblogs.com/xuchunlin/p/7247346.html
"""


def huffman(nodes, frequent):
    trees = list(zip(frequent, nodes))  # num ensures valid ordering
    heapify(trees)  # A min-heap based on freq
    while len(trees) > 1:  # Until all are combined
        value1, node1 = heappop(trees)  # Get the two smallest trees
        value2, node2 = heappop(trees)
        heappush(trees, (value1 + value2, [node1, node2]))  # Combine and re-add them
    # print trees
    return trees[0][-1]


if __name__ == '__main__':
    chars = "fecbda"
    weights = [5, 9, 12, 13, 16, 45]
    print(huffman(chars, weights))  # ['a', [['c', 'b'], [['f', 'e'], 'd']]]
