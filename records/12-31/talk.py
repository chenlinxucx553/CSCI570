__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 10:57 AM'

string = input()
code = list(input())

encoded_str = []
for c in string:
    if c.isdigit() is True or c.isalpha() is True:
        encoded_str.append(1)
    else:
        encoded_str.append(0)

same_count = 0
for a, b in zip(encoded_str, code):
    if int(a) == int(b):
        same_count += 1

print("%.2f%%" % (same_count / len(code) * 100))
# print(str(round(same_count / len(code) * 100, 2)) + "%")
# print("%.2f%%" % (same_count / float(len(code)) * 100))

ch = input()
x = []
count = 0
for i in ch:
    if i.isdigit() is True or i.isalpha() is True:
        x.append('1')
    else:
        x.append('0')
num = list(input())
for i, j in zip(num, x):
    if i == j:
        count += 1
print("%.2f%%" % (count / float(len(ch)) * 100))
