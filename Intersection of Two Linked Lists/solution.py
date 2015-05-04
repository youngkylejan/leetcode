# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        
        p = headA
        q = headB

        while p and q:
            p = p.next
            q = q.next

        while p:
            p = p.next
            headA = headA.next

        while q:
            q = q.next
            headB = headB.next

        while headA and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA