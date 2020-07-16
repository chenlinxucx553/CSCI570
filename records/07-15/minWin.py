__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/15/2020 9:39 AM'

import collections


def minWindow(s: str, t: str) -> str:
    need = dict.fromkeys(t, 1)
    i = 0
    res = []
    for j, c in enumerate(s):
        if c in need.keys():
            need[c] -= 1
        else:
            need[c] = -1

        if all(list(map(lambda v: v <= 0, need.values()))):
            for vc in s[i: j]:
                if vc in t:
                    if need[vc] < 0:
                        need[vc] += 1
                        i += 1
                    else:
                        res.append(((i, j + 1), s[i:j + 1]))
                        break
                else:
                    i += 1
            break
    print(res)
    return ""


def minWin(s: str, t: str) -> str:
    need = collections.Counter(t)
    i = 0
    res = ""
    for j, c in enumerate(s):
        if c not in need:
            continue
        need[c] -= 1
        while s[i] not in need or need[s[i]] < 0:
            if s[i] in need: need[s[i]] += 1
            i += 1

        if all(list(map(lambda v: v <= 0, need.values()))):
            if res is "" or len(res) > j - i + 1:
                res = s[i: j + 1]
    return res


if __name__ == '__main__':
    S = "a"
    T = "aa"

    print(minWin(S, T))
