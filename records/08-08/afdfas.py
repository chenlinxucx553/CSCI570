__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/8/2020 12:37 AM'

import collections


def update_dict(table, record):
    table[record[0]].add(record[1])
    need2update = {record[1]}
    visited = set()
    while need2update:
        other = need2update.pop()
        if other in table.keys() and other not in visited:
            need2update.update(table[other])
            table[record[0]].update(table[other])
            visited.add(other)


if __name__ == "__main__":
    n, m = map(int, input().split())

    table = collections.defaultdict(set)
    ans = 0
    for _ in range(m):
        record = tuple(map(int, input().split()))
        update_dict(table, record)

    # ans = 0
    # visited = set()
    # for key in table.keys():
    #     for prefer in list(table[key]):
    #         if key != prefer and key in table[prefer] and (prefer, key) not in visited:
    #             ans += 1
    #             visited.add((prefer, key))

    print(ans // 2 + 1)
