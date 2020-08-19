__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/14/2020 10:57 PM'

s = input().strip()
a = []
left = 0
for i in s:
    if i == '(':
        left += 1
        continue
    if left:
        if i == ')':
            left -= 1
        continue
    if i == '<':
        a.pop()
    else:
        a.append(i)
s = ''.join(a)
print(s)
