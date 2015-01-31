# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.tail = None
        self.pre = TreeNode(-9999999)
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if root is None:
            return root
        self.dfs(root)
        tmp = self.first.val
        print tmp
        if self.second is None:
            print self.tail.val
            self.first.val = self.tail.val
            self.tail.val = tmp
        else:
            print self.second.val
            self.first.val = self.second.val
            self.second.val = tmp
        return root
    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        if self.first is None and self.pre.val >= root.val:
            self.first = self.pre
            self.tail = root
        elif self.first is not None and self.pre.val >= root.val:
            self.second = root
                self.pre = root
            self.dfs(root.right)