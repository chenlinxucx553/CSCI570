__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/1/2020 10:39 AM'

import networkx
import matplotlib.pyplot as plt


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BTree(object):

    def __init__(self, data):
        self.root = None
        self.insert(data)

    def insert(self, data):
        if data is None:
            return
        if not self.root:
            self.root = Node(data[0])
            data = data[1:]

        for val in data:
            current_root = self.root
            while True:
                if val > current_root.value:
                    if not current_root.right:
                        current_root.right = Node(val)
                        break
                    else:
                        current_root = current_root.right
                else:
                    if not current_root.left:
                        current_root.left = Node(val)
                        break
                    else:
                        current_root = current_root.left

    def pre_order(self, root):
        if root is not None:
            print(root.value, end=',')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root.left is not None:
            self.in_order(root.left)
        if root is not None:
            print(root.value, end=',')
        if root.right is not None:
            self.in_order(root.right)

    def post_order(self, root):
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right)
        if root is not None:
            print(root.value, end=',')

    def __create_graph(self, graph, node, x=0, y=0, pos={}, layer=1):
        pos[node.value] = (x, y)
        if node.left:
            graph.add_edge(node.value, node.left.value)
            l_x, l_y = x - 1 / 2 ** layer, y - 1
            l_layer = layer + 1
            self.__create_graph(graph, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            r_x, r_y = x + 1 / 2 ** layer, y - 1
            r_layer = layer + 1
            self.__create_graph(graph, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return graph, pos

    def draw(self, node=None):
        if not node:
            node = self.root
        graph = networkx.DiGraph()
        graph, pos = self.__create_graph(graph, node)
        fig, ax = plt.subplots(figsize=(8, 8))
        networkx.draw_networkx(graph, pos, ax=ax, node_size=300)
        plt.show()


if __name__ == '__main__':
    data = [23, 5, 3, 26, 1, 54, 2, 4, 9, 45, 32]
    tree = BTree(data)
    print("Pre Order: ", end=" ")
    tree.pre_order(tree.root)
    print()
    print("In Order: ", end=" ")
    tree.in_order(tree.root)
    print()
    print("Post Order: ", end=" ")
    tree.post_order(tree.root)
    print()
    tree.draw()
