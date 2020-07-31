__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/26/2020 6:10 PM'

def my_zip(*iterator):
    iterators = [iter(it) for it in iterator]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, '')
            if elem is '':
                return
            result.append(elem)
        yield tuple(result)

def my_enumerate(arr):
    index = 0
    for elem in arr:
        yield index, elem
        index += 1


if __name__ == '__main__':
    qw = ["flower", "flow", "flight"]
    # for c in zip(*qw):
    #     print(c)

    for v in my_zip(*qw):
        print(v)

    for i,v in my_enumerate(qw):
        print(i, v)