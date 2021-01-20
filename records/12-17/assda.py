__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/17/2020 3:20 PM'

from collections import defaultdict, Counter

string = "this is an example for huffman encoding"


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + "0"))
    d.update(huffmanCodeTree(r, False, binString + "1"))
    return d


freq = Counter(string)

wordFrequency = sorted(freq.items(), key=lambda x: -x[1])

while len(wordFrequency) > 1:
    key1, c1 = wordFrequency[-1]
    key2, c2 = wordFrequency[-2]

    wordFrequency = wordFrequency[:-2]

    node = NodeTree(key1, key2)

    wordFrequency.append((node, c1 + c2))
    wordFrequency = sorted(wordFrequency, key=lambda x: -x[1])

huffmanCode = huffmanCodeTree(wordFrequency[0][0])
print(huffmanCode)
