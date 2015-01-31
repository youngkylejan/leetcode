# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
		if root is None:
			return []

		stack = []
		ans = []
		stack.append(root)

		while len(stack) > 0:
			top = stack.pop()
			ans.append(top.val)

			if top.right is not None:
				stack.append(top.right)
			if top.left is not None:
				stack.append(top.left)

		return ans        