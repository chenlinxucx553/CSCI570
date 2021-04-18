__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/8 20:12'

if S(φ) == False:
    return "φ is not satifiable"

for i in range(n):
    if S(φ_i) == True:
        update φ <- φ_i
        update x_i = True
    else:
        update φ < - ! φ_i
        update x_i = False