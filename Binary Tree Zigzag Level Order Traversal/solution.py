# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.ans = []
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.DFS(root, 0)
        for i in range(0, len(self.ans)):
            if i % 2 != 0:
                self.ans[i].reverse()
        return self.ans
    def DFS(self, root, height):
        if root is None:
            return
        if height == len(self.ans):
            self.ans.append([])
        self.ans[height].append(root.val)
        self.DFS(root.left, height + 1)
        self.DFS(root.right, height + 1)