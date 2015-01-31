# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        tail = head
        len = 1
        while tail.next is not None:
            tail = tail.next
            len = len + 1
        k = k % len
        if k == 0:
            return head
        tail.next = head
        for i in range(0, len - k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head