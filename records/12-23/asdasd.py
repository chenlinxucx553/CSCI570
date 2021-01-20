__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/23/2020 10:36 AM'


class Solution:
    def candy(self, ratings) -> int:

        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] > ratings[i]:
                if res[i - 1] > res[i]:
                    pass
                else:
                    res[i - 1] += 1
            elif ratings[i - 1] < ratings[i]:
                res[i] += 1
            elif ratings[i - 1] == ratings[i]:
                pass

        return sum(res)


res = Solution().candy([1, 2, 87, 87, 87, 2, 1])
print(res)


def preorder(self, root):
    result = []

    def dfs(node):
        if node is not None:
            result.append(node.val)

            if node.left is not None:
                dfs(node.left)

            if node.right is not None:
                dfs(node.right)

    dfs(root)
    return result
