# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        p = head
        q = head
        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            if p == q:
                break
        if q is None or q.next is None:
            return None
                    while head != p:
            p = p.next
            head = head.next
        return head