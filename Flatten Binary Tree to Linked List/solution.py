# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.tail = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return
        self.preorder(root)
    def preorder(self, root):
        if root is not None:
            if self.tail is not None:
                self.tail.left = None
                self.tail.right = root
            self.tail = root
            left = root.left
            right = root.right
            self.preorder(left)
            self.preorder(right)