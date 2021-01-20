__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/25/2020 12:10 PM'


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def isValid(row, col):
            """
            # 判断（row,col）是否可行
            :param row:
            :param col:
            :return:
            """

            # 同列有没有皇后
            for c in range(col):
                if board[row][c] == 'Q':
                    return False

            # 同行有没有皇后
            for r in range(row):
                if board[r][col] == 'Q':
                    return False

            # 左上角有没有皇后
            cur_row, cur_col = row, col
            while cur_row > 0 and cur_col > 0:
                cur_row -= 1
                cur_col -= 1
                if board[cur_row][cur_col] == 'Q':
                    return False

            # 右上角有没有皇后
            cur_row, cur_col = row, col
            while cur_row > 0 and cur_col < n - 1:
                cur_row -= 1
                cur_col += 1
                if board[cur_row][cur_col] == 'Q':
                    return False
            return True

        def DFS(res, row):
            """
            回溯法
            :param res:
            :param row:
            :return:
            """

            # 放好了N个皇后，就要开始返回了
            if row == n:
                temp = []
                for line in board:
                    t = ''.join(line)
                    temp.append(t[:])
                res.append(temp[:])
                return

            for col in range(len(board[row])):
                if not isValid(row, col):
                    continue
                board[row][col] = 'Q'
                DFS(res, row + 1)
                board[row][col] = '.'

        DFS(res, 0)
        return res
