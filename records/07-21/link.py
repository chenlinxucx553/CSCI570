__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/22/2020 10:10 PM'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return self.head



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None

        stack = []
        while head.next is not None:
            stack.append(head.val)
            head = head.next

        stack.append(head.val)

        res = ListNode(stack.pop())
        p = res
        while len(stack) > 0:
            temp = ListNode(stack.pop())
            p.next = temp
            p = p.next

        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    link = ListNode(-1).initList(arr)
    Solution().reverseList(link)
