class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):

		if root is None:
			return True

		if abs(self.height(root.left) - self.height(root.right)) > 1:
			return False

		return self.isBalanced(root.left) and self.isBalanced(root.right)

	def height(self, root):
		if root is None:
			return 0

		return max(self.height(root.left) + 1, self.height(root.right) + 1)
