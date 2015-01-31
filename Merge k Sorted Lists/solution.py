# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) <= 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)
    def divide(self, lists, start, end):
        if start + 1 == end:
            return self.merge(lists[start], lists[end])
        if start == end:
            return lists[start]
        mid = (start + end) / 2
        return self.merge(self.divide(lists, start, mid), self.divide(lists, mid + 1, end))
    def merge(self, l1, l2):
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1 is not None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2 is not None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return head.next