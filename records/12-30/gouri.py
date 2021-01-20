__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/30/2020 8:28 PM'

# check = input()
# check_i = check[::-2]
# check_u = check[:len(check) - 1]
# check_u = check_u[::-2]
# a_li = [int(i) for i in check_i]
# b_li = [int(i) for i in check_u]
# sum = 0
# for i in a_li:
#     sum = sum + int(i)
# for i in b_li:
#     k = int(i) * 2
#     if k >= 10:
#         k = k - 9
#     sum = sum + int(k)
# if sum % 10 == 0:
#     print("ok")
# else:
#     print("error")


while 1:
    code = input()

    odd_sum, even_sum = 0,0
    for i in range(len(code) - 1, 0, -2):
        odd_sum += int(code[i])
        temp = int(code[i - 1]) * 2
        if temp >= 10:
            temp -= 9
        even_sum += temp

    print('ok' if (odd_sum + even_sum) % 10 == 0 else 'error')
