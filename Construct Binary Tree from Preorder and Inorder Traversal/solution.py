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
    def buildTree(self, preorder, inorder):
        if len(inorder) <= 0:
            return None
        root = self.process(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
        return root
    def process(self, preorder, inorder, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd:
            return None
        root = TreeNode(preorder[preStart])
        i = inStart
        for i in range(inStart, inEnd + 1):
            if inorder[i] == root.val:
                break
        root.left = self.process(preorder, inorder, preStart + 1, preStart + i - inStart, inStart, i - 1
)
        root.right = self.process(preorder, inorder, preEnd - inEnd + i + 1, preEnd, i + 1, inEnd)
        return root