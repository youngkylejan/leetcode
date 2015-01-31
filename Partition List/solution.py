# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None:
            return head
        tmp = ListNode(0)
        tmp.next = head
        pre = tmp
        tail = ListNode(0)
        p = tail
        while head is not None:
            if head.val >= x:
                p.next = ListNode(head.val)
                p = p.next
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        pre.next = tail.next
        return tmp.next