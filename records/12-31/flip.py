__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 10:29 AM'

while 1:
    a = int(input())
    nums = list(map(int, input().split(' ')))

    if a == 1:
        print('yes')
        break
    i, j = 0, 1
    flag = True

    while i < len(nums) - 1:
        if nums[i] < nums[i + 1]:
            i += 1
        else:
            if flag:
                j = i + 1
                while j < len(nums) - 1:
                    if nums[j - 1] > nums[j]:
                        j += 1
                    else:
                        break
                nums[i:j] = reversed(nums[i:j])
                flag = False
            else:
                print('no')

    print('yes')
