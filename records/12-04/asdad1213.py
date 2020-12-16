__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/4/2020 11:00 PM'

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

from collections import Counter


class Solution:
    def leastInterval(self, tasks, n) -> int:
        if not tasks:
            return 0
        counter = Counter(tasks)

        max_task = max(counter, key=counter.get)
        min_time = (counter[max_task] - 1) * (n + 1) + 1

        for k, v in counter.items():
            if v == counter[max_task] and k != max_task:
                min_time += 1
        return max(min_time, len(tasks))


res = Solution().leastInterval(tasks, n)
print(res)
