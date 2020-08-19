import copy
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        if not s: return ""

        remove = []
        stack = []
        for i, c in enumerate(s):
            if c is '(':
                stack.append(i)
            elif c is ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    remove.append(i)

        if stack or remove:
            s = list(s)
            for i in stack: s[i] = ''
            for j in remove: s[j] = ''

        return ''.join(s)


if __name__ == '__main__':
    ste = "lee(t(c)o)de)"
    ss = Solution().minRemoveToMakeValid(ste)
    print(ss)
