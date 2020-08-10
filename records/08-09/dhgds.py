__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 4:18 PM'

class Solution:

    # 1. 统计该字符串中需要最少删除多少个左右括号才能保证有效。
    def get_remove_num(self, s: str):
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
            if c == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    # 2. 判断字符串是否合法有效。
    def is_valid(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    # 3. 回溯方法
    def removeInvalidParentheses(self, s: str):
        rm_left, rm_right = self.get_remove_num(s)
        ans = []
        def dfs(left: int, right: int, start: int, ss: str):
            if left == right == 0 and self.is_valid(ss):
                ans.append(ss)
            for i in range(start, len(ss)):
                c = ss[i]
                # 去重复
                if i > 0 and ss[i] == ss[i-1]:
                    continue
                if c == "(" and left > 0:
                    dfs(left - 1, right, i, ss[:i] + ss[i + 1:])
                elif c == ")" and right > 0:
                    dfs(left, right - 1, i, ss[:i] + ss[i + 1:])
        dfs(rm_left, rm_right, 0, s)
        return ans

    # 4. BFS广度优先搜索方法, 搜到有效的字符串时就可以在当前层结束后返回。
    def removeInvalidParentheses2(self, s: str):
        rm_left, rm_right = self.get_remove_num(s)
        ans = []
        def dfs(left: int, right: int, start: int, ss: str):
            if left == right == 0 and self.is_valid(ss):
                ans.append(ss)
            for i in range(start, len(ss)):
                c = ss[i]
                # 去重复
                if i > 0 and ss[i] == ss[i-1]:
                    continue
                if c == "(" and left > 0:
                    dfs(left - 1, right, i, ss[:i] + ss[i + 1:])
                elif c == ")" and right > 0:
                    dfs(left, right - 1, i, ss[:i] + ss[i + 1:])
        dfs(rm_left, rm_right, 0, s)
        return ans
