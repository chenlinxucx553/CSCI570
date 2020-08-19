__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/11/2020 4:59 PM'


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        seg1 = version1.split('.')
        seg2 = version2.split('.')

        def fill(arr, count):
            while count:
                arr.append('0')
                count -= 1

        if len(seg1) > len(seg2):
            fill(seg2, len(seg1) - len(seg2))
        else:
            fill(seg1, len(seg2) - len(seg1))

        for val1, val2 in zip(seg1, seg2):
            if int(val1) == int(val2):
                continue
            else:
                if int(val1) < int(val2):
                    return -1
                else:
                    return 1

        return 0


if __name__ == '__main__':
    version1 = "1.1"
    version2 = "1.1"

    res = Solution().compareVersion(version1, version2)
    print(res)
