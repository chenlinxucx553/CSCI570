__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/17/2020 4:59 PM'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        if n <= 0: return []

        def helper(start, end):
            if start > end: return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        tree = TreeNode(i)
                        tree.left = left
                        tree.right = right
                        all_trees.append(tree)
            return all_trees

        return helper(1, n)
