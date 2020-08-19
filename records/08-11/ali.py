__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/11/2020 5:40 PM'

def get_num_of_one(num):
    count = 0
    for i in bin(num)[2:]:
        if i == '1':
            count += 1
    return count

res = get_num_of_one(12)
print(res)