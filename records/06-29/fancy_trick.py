__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/29/2020 11:37 AM'

def merge_dictionaries(a, b):
   return {**a, **b}


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b))
# {'y': 3, 'x': 1, 'z': 4}


def most_frequent(list):
    print(list.count(1)) # 3
    return sorted(set(list), key = list.count, reverse = True)


list = [1,2,1,2,3,2,1,4,2]
print(most_frequent(list))
print(list[::-1])