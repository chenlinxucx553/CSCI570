__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/30/2020 3:26 PM'


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return False
        if p == '*': return True
        if p == '?' and len(s) == 1:
            return True
        elif p == '?' and len(s) > 1:
            return False

        m, n = len(s), len(p)
        i, j = 0, 0
        flag = False
        next_c = ''
        while i < m and j < n:
            if flag:
                if next_c == s[i]:
                    i += 1
                    j += 1
                    flag = False
                    continue
                else:
                    i += 1
                    continue

            if s[i] == p[j]:
                i += 1
                j += 1
                continue
            elif p[j] == "?":
                j += 1
                continue
            elif p[j] == "*":
                i += 1
                flag = True
                if j + 1 < n:
                    next_c = p[j + 1]
                else:
                    return True
            else:
                return False


if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    print(Solution().isMatch(s, p))
