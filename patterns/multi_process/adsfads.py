__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/4/2020 9:34 PM'

if __name__ == '__main__':

    def subsets(arr):
        if len(arr) == 0:
            return [arr]
        else:
            temp = []
            sub_result = subsets(arr[1:])
            for item in sub_result:
                temp.append([arr[0]] + item)

            return sub_result + temp


    print(subsets([1, 2, 3, 4]))
