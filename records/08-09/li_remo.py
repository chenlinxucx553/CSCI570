__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 3:48 PM'


class Solution:

    def go_check(self):
        candidate = []
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][1] == ")":
                candidate.append(i)
        return candidate

    def removeInvalidParentheses(self, s: str):

        if not s: return [""]
        if len(s) == 1:
            if s[0].isalpha():
                return s
            else:
                return [""]

        self.stack = []
        s_copy = s
        ans = set()
        for i, c in enumerate(s):
            if c != ")":
                # alpha or (
                self.stack.append((i, c))
            else:
                if self.stack:
                    if self.stack[-1][1] == '(' or str(self.stack[-1][1]).isalpha():
                        self.stack.append((i, c))
                        continue
                    else:
                        candidate_index = self.go_check()
                        temp = list(s_copy)
                        # del temp[i]
                        for index in candidate_index:
                            ans.add(''.join(temp[:index] + temp[index + 1:]))

        return list(ans) if ans else [""]

    def removeInvalidParentheses2(self, s: str):
        def isValid(s):
            cursum = 0
            for x in s:
                if x == '(':
                    cursum += 1
                if x == ')':
                    cursum -= 1
                if cursum < 0:
                    return False
            return cursum == 0

        # BFS:
        cur_level = set()
        cur_level.add(s)
        while True:
            valids = list(filter(isValid, cur_level))
            if valids:
                return valids
            next_level = set()
            for s in cur_level:
                # 遍历所有删掉一个括号的情况
                for i in range(len(s)):
                    if s[i] in ['(', ')']:
                        next_level.add(s[:i] + s[i + 1:])
            cur_level = next_level


if __name__ == '__main__':
    ss = "(a)())()"
    Solution().removeInvalidParentheses2(ss)
