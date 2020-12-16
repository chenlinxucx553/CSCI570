__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2020 6:12 AM'

from collections import defaultdict

while True:
    try:
        T = int(input().split()[0])
        data = []
        res = []
        for _ in range(T):
            n = int(input().split()[0])
            nums_set_dict = defaultdict(list)
            for i in range(n):
                vals = list(map(int, input().split()))
                val_set = frozenset(sorted(vals))
                nums_set_dict[val_set].append(i)
                data.append(vals)

            test = list(map(lambda val: len(val) >= 2, nums_set_dict.values()))
            if any(list(map(lambda val: len(val) >= 2, nums_set_dict.values()))):
                res.append("YES")
            else:
                res.append("NO")

        print("\n".join(res))


    except:
        break
