# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
	def __init__(self):
		self.ans = -10000000

	def maxPathSum(self, root):
		self.getMax(root)
		return self.ans

	def getMax(self, root):
		if root is None:
			return 0
		else:
			a = self.getMax(root.left)
			b = self.getMax(root.right)
			value = root.val
			value = value + (0, a)[a > 0]
			value = value + (0, b)[b > 0]

			if value > self.ans:
				self.ans = value

			if a > b and a > 0:
				return root.val + a
			if b > a and b > 0:
				return root.val + b

			return root.val