__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 4:54 PM'

n_m = list(map(int, input().split()))
n, m = n_m[0], n_m[1]
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input().strip()))))

moves = 0
for i in range(0, int(n / 2)):
    for j in range(0, int(m / 2)):
        temp = matrix[i][j] \
               + matrix[n - 1 - i][j] \
               + matrix[i][m - 1 - j] \
               + matrix[n - 1 - i][m - 1 - j];
        if temp == 2:
            moves += 2
        elif temp < 2:
            moves += temp
        else:
            moves += 4 - temp

if n % 2 == 1:
    for j in range(0, int(m / 2)):
        if matrix[int(n / 2)][j] != matrix[int(n / 2)][m - 1 - j]:
            moves += 1

if m % 2 == 1:
    for j in range(0, int(n / 2)):
        if matrix[j][int(m / 2)] != matrix[n - 1 - j][int(m / 2)]:
            moves += 1

print(moves)
