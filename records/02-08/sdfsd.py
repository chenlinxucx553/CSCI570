__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/10/2021 7:40 PM'

if __name__ == '__main__':
    length = 0
    S = ""
    S_prime = ""
    for i in range(len(S)):
        if length == len(S_prime):
            break
        if S[i] == S_prime[length]:
            length += 1

    if length == len(S_prime):
        print("yes")
    else:
        print("no")
