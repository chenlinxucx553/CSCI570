__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 3:41 PM'


class Solution:

    def addSome(self, index, num):
        self.arr[index] += num
        carry = self.arr[index] // 10
        self.arr[index] %= 10
        return carry

    def plusOne(self, digits):
        self.arr = digits
        carry = self.addSome(len(digits) - 1, 1)

        j = len(digits) - 2
        while carry != 0:
            if 0 <= j:
                carry = self.addSome(j, carry)
                j -= 1
            else:
                self.arr.insert(0, carry)
                carry = 0
        return self.arr


if __name__ == '__main__':
    num = [9, 9, 9]
    res = Solution().plusOne(num)
    print(res)
