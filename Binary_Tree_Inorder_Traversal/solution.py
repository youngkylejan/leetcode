# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        inorder = []
    
        while root is not None or len(stack) > 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                inorder.append(temp.val)
                root = temp.right
    
        return inorder