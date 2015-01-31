# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k is None:
            return None
        root = ListNode(0)
        root.next = head
        pre = root
        first = head
        p = head
        interval = 0
        while p is not None:
            interval = interval + 1
            p = p.next
            second = None
            if interval == k:
                second = first.next
                first.next = p
                nextPre = first
                                while second != p and second is not None:
                    tmp = second.next
                    second.next = first
                    first = second
                    second = tmp
                interval = 0
                pre.next = first
                pre = nextPre
                first = p
            if p is None:
                break
        return root.next