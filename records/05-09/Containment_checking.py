__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '5/9/2020 11:12 PM'

if __name__ == '__main__':
    numbers = [1, 2, 3, 5, 7]
    squares = (n ** 2 for n in numbers)

    # print(list(squares)) # [1, 4, 9, 25, 49]
    print(squares)
    # print(9 in squares) # False
    # print(list(squares)) # []
    # print(9 in squares)
    # the value in generator only can use once
