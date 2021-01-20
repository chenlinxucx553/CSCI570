__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 11:20 AM'

n, l = map(int, input().split())
pos = list(map(int, input().split()))

pos.sort()
distance = []
for i in range(len(pos) - 2):
    distance.append((pos[i + 1] - pos[i]) / 2)

distance.append(pos[0])
distance.append(l - pos[-1])
distance.sort()

print("%.2f" % distance[-1])
