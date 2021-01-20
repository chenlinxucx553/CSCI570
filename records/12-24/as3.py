__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/25/2020 12:07 PM'


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            while node.children:
                stack.append(node.children.pop())

        return result
