# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if head is None or head.next is None:
            return head

        p = head
        q = head.next

        pre = ListNode(p.val)
        rhead = ListNode(q.val)

        count = 1
        while q is not None:
            rhead.next = pre
            pre = rhead
            count = count + 1

            p = p.next
            q = q.next

            if q is None:
                break

            rhead = ListNode(q.val)

        p = head
        q = rhead

        flag = count % 2

        while True:
            count = count - 2
            p1 = p.next
            q1 = q.next

            p.next = q
            q.next = p1

            if count == 0 and flag == 0:
                q.next = None
                break

            if count == 1 and flag == 1:
                p1.next = None
                break

            p = p1
            q = q1

        return head