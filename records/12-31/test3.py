__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 10:15 PM'

while 1:
    num = int(input().strip())

    if num >= 0:
        bin_str = '{:016b}'.format(num)
        hex_str = (", %04X" % num)
    else:
        bin_str = bin(2 ** 16 + num)[2:]
        hex_str = (", %04X" % (num & 0xFFFF))

    print(bin_str + hex_str)