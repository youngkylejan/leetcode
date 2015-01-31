# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or m >= n:
            return head
        pos = 0
        prePos = 0
        root = ListNode(0)
        root.next = head
        p = root
        q = root.next
        first = None
        second = None
        pre = None
        tail = None
        while q is not None:
            if first is None and pos + 1 == m:
                pre = p
                prePos = pos
                first = q
            if first is not None and pos + 1 == n:
                second = q
                tail = q.next
                break
            pos = pos + 1
            p = p.next
            q = q.next
        p = first
        q = p.next
        tmp = q.next if q is not None else None
        while p != second:
            q.next = p
            p = q
            if q == second:
                break
            q = tmp
            tmp = tmp.next
        pre.next = second
        first.next = tail
        return pre.next if prePos == 0 else head