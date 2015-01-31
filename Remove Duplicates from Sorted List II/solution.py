# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        pre = ListNode(0)
        pre.next = head
        p = head
        q = head.next
        head = pre
        while q is not None:
            if p.val == q.val:
                while p.val == q.val:
                    p = p.next
                    q = q.next
                    if q is None:
                        break
                pre.next = q
                p = q
                if q is None:
                    break
                q = q.next
            else:
                pre = p
                p = p.next
                q = q.next
        return head.next