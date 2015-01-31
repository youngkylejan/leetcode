# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) <= 0:
            return None
        root = self.process(inorder, postorder, len(inorder))
        return root
    def process(self, inorder, postorder, length):
        if length - 1 < 0:
            return
        root = TreeNode(postorder[length - 1])
        for i in range(0, length):
            if inorder[i] == root.val:
                break
        root.left = self.process(inorder, postorder, i)
        root.right = self.process(inorder[i + 1 : length], postorder[i : length], length - i - 1)
        return root