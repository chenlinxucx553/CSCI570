__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 11:43 PM'


while True:
    try:
        n, m = map(int, input().split())
        grades = list(map(int, input().split()))
        for _ in range(m):
            command = input().split()
            symbol = command[0]
            a = int(command[1])
            b = int(command[2])
            if symbol == "Q":
                if a > b:
                    a, b = b, a
                print(max(grades[a - 1: b]))
            else: grades[a - 1] = b
    except:
        break

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)