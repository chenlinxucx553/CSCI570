from heapq import heappush, heappop, heapify
from collections import defaultdict, Counter


def encode(charFrequency):
    heap = [[v, [k, ""]] for k, v in charFrequency.items()]
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


txt = "this is an example for huffman encoding"
wordCounter = Counter(txt)
tree = encode(wordCounter)
print("Symbol\tWeight\tHuffman Code")
for p in tree:
    print("%s\t%s\t%s" % (p[0], wordCounter[p[0]], p[1]))
