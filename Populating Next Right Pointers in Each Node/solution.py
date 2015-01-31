# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        root.next = None
        p = root
                self.dfs(p)
    def dfs(self, root):
        if root and root.left:
            root.left.next = root.right
            self.dfs(root.left)
            root.right.next = None if root.next is None else root.next.left
            self.dfs(root.right)