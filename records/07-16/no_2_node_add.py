__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/16/2020 6:48 PM'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def add(self, val1, val2, carry) -> ListNode:
        if (val1 + val2 + carry) >= 10:
            val = (val1 + val2 + carry) % 10
            carry = 1
        else:
            val = val1 + val2
            carry = 0

        return ListNode(val), carry

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        res = ListNode(None)
        dummy.next = res
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            res.next = ListNode(carry % 10)
            res = res.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
