# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        p = head
        q = head
        while p is not None:
            p = p.next
                        if q.next is not None:
                q = q.next.next
            else:
                return False
            if q is None:
                return False
            if p == q:
                return True
        return False