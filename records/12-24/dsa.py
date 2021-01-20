__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/25/2020 10:35 AM'


class Solution:
    def preorder(self, root: 'Node'):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            temp = stack.pop()
            result.append(temp.val)
            if temp.children:
                for item in temp.children[::-1]:
                    stack.append(item)
        return result


class Solution2:
    def preorder(self, root: 'Node'):

        result = []

        def dfs(one_node):
            if root is not None:
                result.append(one_node.val)

                for child in one_node.children:
                    dfs(child)

        dfs(root)
        return result


def preorder(root):
    result = []
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


class Solution3:
    def preorder(root):
        result = []

        stack = [root]
        node = stack[0]
        while stack:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result
