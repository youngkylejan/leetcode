# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.ans = 0
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None:
            return 0
        self.ans = 0
        path = []
        self.dfs(root, path)
        return self.ans
    def dfs(self, root, path):
        if root.left is None and root.right is None:
            self.ans = self.ans + int("".join(path + [str(root.val)]))
            return
        if root.left is not None:
            self.dfs(root.left, path + [str(root.val)])
        if root.right is not None:
            self.dfs(root.right, path + [str(root.val)])