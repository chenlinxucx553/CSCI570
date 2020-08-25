__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/20/2020 4:45 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)

    return wrapper


@show
def minWindow2(s: str, t: str) -> str:
    if not s: return ""
    if not t: return s

    m = len(s)
    import collections
    t_dict = collections.Counter(t)

    flag = 0
    start = 0
    ans = ''
    for end, char in enumerate(s):
        if char in t_dict:
            t_dict[char] -= 1
        else:
            continue

        if t_dict[char] == 0:
            flag += 1

        while s[start] not in t_dict or t_dict[s[start]] < 0:
            if s[start] in t_dict: t_dict[s[start]] += 1
            start += 1

        if flag == len(t_dict):
            if not ans or len(ans) > end - start + 1:
                ans = s[start: end + 1]

    return ans


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"

    minWindow2(S, T)
