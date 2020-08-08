__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 3:24 PM'

if __name__ == '__main__':
    key_dict = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    digits = "23"

    import copy

    res = []
    for c in digits:
        temp = key_dict[int(c)]
        if not res:
            res.extend(temp)
        else:
            temp_res = []
            for i in range(len(res)):
                for new_c in temp:
                    temp_res.append(res[i] + new_c)

            res = temp_res

    print(res)
