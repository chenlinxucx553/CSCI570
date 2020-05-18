__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/23/2020 4:44 PM'

if __name__ == '__main__':
    a = 'a'
    print(a > 'b' or 'c')
    print(0 or 'c')

"""
由于比较运算符优先级大于逻辑运算符，，当 a > 'b'，即 'a' > 'b' 为 Fasle 
时（'a' 的 ASCII 码比 ‘b’ 小），返回值为 'c'，故答案选C
"""
