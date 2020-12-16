__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2020 9:31 PM'


class Solution:

    def my_zip(self, *iterator):
        iterators = [iter(it) for it in iterator]
        size = len(iterator[0])
        while size > 0:
            result = []
            for it in iterators:
                elem = next(it, '')
                result.append(elem)
            yield tuple(result)
            size -= 1

    def transpose(self, A):
        return [list(i) for i in self.my_zip(*A)]


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6]]
    res = Solution().transpose(arr)
    print(res)
