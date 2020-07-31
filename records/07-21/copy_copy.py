__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/22/2020 10:26 PM'

a = ['hello', [1, 2, 3]]
b = a[:]
print("a -> ", [id(x) for x in a])

print("b -> ", [id(x) for x in b])
a[0] = 'world'
print("a -> ", [id(x) for x in a])
a[1].append(4)
print(a)
print("a -> ", [id(x) for x in a])
print("b -> ", [id(x) for x in b])
