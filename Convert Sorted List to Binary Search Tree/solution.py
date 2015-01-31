# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        tail = None
        return self.process(head, tail)
    def process(self, head, tail):
        if head is tail:
            return None
        if head.next is tail:
            root = TreeNode(head.val)
            return root
        p = head
        q = head
        while q is not tail and q.next is not tail:
            q = q.next.next
            p = p.next
        root = TreeNode(p.val)
        root.left = self.process(head, p)
        root.right = self.process(p.next, tail)
        return root