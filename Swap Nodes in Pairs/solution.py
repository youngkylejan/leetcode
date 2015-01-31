# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        p = head
        q = head.next
        pre = None
        count = 0
        while q is not None:
            tmp = q.next
            q.next = p
            p.next = tmp
            if pre is not None:
                pre.next = q
            if count == 0:
                head = q
                count = 1
            pre = p
            p = p.next
            if p is None:
                break
            q = p.next
        return head