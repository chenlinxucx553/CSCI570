__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/23/2020 4:01 PM'

"""
共轭复数，两个实部相等，虚部互为相反数的复数互为共轭复数(conjugate complex number)。
当虚部不为零时，共轭复数就是实部相等，虚部相反,如果虚部为零，其共轭复数就是自身
（当虚部不等于0时也叫共轭虚数）。复数z的共轭复数记作z（上加一横），有时也可表示为Z*。
同时, 复数z（上加一横）称为复数z的复共轭(complex conjugate)。
"""

if __name__ == '__main__':
    a = 1 + 2j  # how to define a complex => j or J both are ok
    b = 2 - 3J
    print(a.conjugate())  # (1-2j)
    print(b.conjugate())  # (2+3j)

    # complex = real + imaginary
    print("{} -> {}".format(a.real, type(a.real)))
    print("{} -> {}".format(a.imag, type(a.imag)))


"""
(1-2j)
(2+3j)
1.0 -> <class 'float'>
2.0 -> <class 'float'>
"""