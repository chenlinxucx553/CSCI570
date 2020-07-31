__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/30/2020 2:58 PM'


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_i = (i // 3) * 3 + j // 3
                    num = int(board[i][j])
                    row[i].remove(num)
                    col[j].remove(num)
                    box[box_i].remove(num)
                else:
                    empty.append((i, j))

        def sort_empty(ipt):
            i, j = ipt
            box_i = (i // 3) * 3 + j // 3
            return len(row[i] & col[j] & box[box_i])

        def backtrack():
            # search fewest candidates first
            empty.sort(key=sort_empty)  # sort the list IN PLACE
            if len(empty) == 0:
                # terminator
                return True

            i, j = empty.pop(0)
            box_i = (i // 3) * 3 + j // 3
            # for ll in cands:
            for val in row[i] & col[j] & box[box_i]:
                row[i].remove(val)
                col[j].remove(val)
                box[box_i].remove(val)
                board[i][j] = str(val)
                if backtrack():
                    return True
                row[i].add(val)
                col[j].add(val)
                box[box_i].add(val)
            empty.append((i, j))
            return False

        backtrack()


if __name__ == '__main__':
    arr = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    Solution().solveSudoku(arr)

    print(arr)
