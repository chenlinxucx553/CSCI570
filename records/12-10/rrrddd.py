__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/10/2020 10:50 AM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


from collections import defaultdict


class Solution:
    @show
    def predictPartyVictory(self, senate: str) -> str:
        r_d = defaultdict(list)
        for i, c in enumerate(senate):
            r_d[c].append(i)

        temp = []
        for key, val in r_d.items():
            temp.append((key, len(val), sum(list(val))))

        temp.sort(key=lambda item: (-item[1], item[2]))

        return "Radiant" if temp[0][0] == 'R' else "Dire"


ss = "RD"
Solution().predictPartyVictory(ss)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        import heapq
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1
