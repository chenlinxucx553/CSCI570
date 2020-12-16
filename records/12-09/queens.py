__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/9/2020 11:46 AM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


@show
def test(n):
    res = []
    board = [['.'] * n for _ in range(n)]  # 初始化棋盘

    def isValid(row, col):
        if len(list(filter(lambda val: val == 'Q', [i[col] for i in board[:row]]))) >= 1:
            return False

        if len(list(filter(lambda val: val == 'Q', board[row][:col]))) >= 1:
            return False

        mrow, mcol = row, col# 左上
        while mrow > 0 and mcol > 0:  # mrow:0->row-1,mcol:0->row-1
            mrow -= 1
            mcol -= 1
            if board[mrow][mcol] == 'Q': return False

        vrow, vcol = row, col # 右上
        while vrow > 0 and vcol < n - 1:  # vrow:0->row-1,vcol:col+1->n
            vrow -= 1
            vcol += 1
            if board[vrow][vcol] == 'Q': return False
        return True

    def backtrace(n, row):
        if row == n:
            temp = []
            for line in board:
                temp.append(''.join(line))
            res.append(temp)
            return

        for col in range(len(board[row])):
            if not isValid(row, col):
                continue
            board[row][col] = 'Q'
            backtrace(n, row + 1)
            board[row][col] = '.'
        pass

    backtrace(n, 0)
    return res


test(4)

# n = 4
# board = [[str(_ + __) for _ in range(n)] for __ in range(n)]
#
# print(board)
# row = 2
# col = 2
# print(board[row][:2])

# for r in range(row):  # r:0->row-1
#     print(board[r][col])