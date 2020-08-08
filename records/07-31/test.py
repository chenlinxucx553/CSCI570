__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/30/2020 11:26 PM'

if __name__ == '__main__':
    original_str = "ldbsascbl"
    i,j = 0, len(original_str) - 1

    A = []
    while i < j:
        if original_str[i] == original_str[j]:
            A.append(original_str[i])
            i += 1
            j -= 1
        else:
            if i < j and i + 1 < j and original_str[i + 1] == original_str[j]:
                i += 1
            elif i < j and j - 1 > i and original_str[i] == original_str[j - 1]:
                j -= 1
    print(len(A) * 2)