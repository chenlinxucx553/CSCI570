__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/27/2020 4:08 PM'


# Huffman Encoding

# Tree-Node Type
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


# create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


# Huffman编码
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


if __name__ == '__main__':
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    freqs = [10, 4, 2, 5, 3, 4, 2, 6, 4, 4, 3, 7, 9, 6]
    chars_freqs = zip(chars, freqs)
    chars_freqs = sorted(chars_freqs, key=lambda item: item[1])
    nodes = [Node(item[1]) for item in chars_freqs]
    root = createHuffmanTree(nodes)
    encoding_map = huffmanEncoding(nodes, root)
    for item in zip(chars_freqs, encoding_map):
        print('Character:%s freq:%-2d   encoding: %s' % (item[0][0], item[0][1], item[1]))
