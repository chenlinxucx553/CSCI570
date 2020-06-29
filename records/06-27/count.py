__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/27/2020 12:08 PM'

from collections import Counter
from functools import reduce
from operator import add

if __name__ == '__main__':
    s = "dfasvdfkjaasfgajsasufygasbwrewqkjoascnxmcvcasugdfwieoier" \
        "nkaspozmzzxjcgushkbwevdsuvgaowbdjasdgdvervnbassgoahgbqf"


    # counter = Counter(s)
    # print(counter)

    def mapper(a):
        return (a, 1)


    def reducer(x, y):
        if isinstance(x, dict):
            ykey, yval = y
            if ykey not in x:
                x[ykey] = yval
            else:
                x[ykey] += yval
            print(x)
            return x
        else:
            xkey, xval = x
            ykey, yval = y
            a = {xkey: xval}
            if ykey in a:
                a[ykey] += yval
            else:
                a[ykey] = yval
            return a


    mapred = reduce(reducer, map(mapper, s))

    print(mapred.items())