__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '1/2/2021 9:53 AM'


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        left_temp = ListNode(None)
        right_temp = ListNode(None)
        left = left_temp
        right = right_temp

        while head:
            temp = ListNode(head.val)
            if head.val < x:
                left_temp.next = temp
                left_temp = left_temp.next
            else:
                right_temp.next = temp
                right_temp = right_temp.next

            head = head.next

        left_temp.next = right.next

        return left.next
