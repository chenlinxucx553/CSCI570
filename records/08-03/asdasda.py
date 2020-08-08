__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/3/2020 3:29 PM'


# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         if not logs: return []
#
#         alpha_log = []
#         numeric_log = []
#         for item in logs:
#             ks = item.split()
#             if ks[1].isalpha():
#                 alpha_log.append((ks[0], ks[1:]))
#             else:
#                 numeric_log.append((ks[0], ks[1:]))
#
#         ss = sorted(alpha_log, key=lambda item: (item[1], item[0]))
#
#         print(ss)


if __name__ == '__main__':

    st1213 = "1234"
    arr = [1,2,3,4]
    print(st1213[1:4])
    print(arr[1:4])