class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		if root is None:
			return True

		if root.left is None and root.right is None:
			return True

		arr = [root.val]

		return self.dfs(root.left, arr, [-1]) and self.dfs(root.right, arr, [1])

	def dfs(self, root, arr, side):

		if root is None:
			return True

		for i in range(len(side) - 1, -1, -1):
			if side[i] == -1 and root.val >= arr[i]:
				return False
			if side[i] == 1 and root.val <= arr[i]:
				return False

		tmp = arr + [root.val]

		if root.left is None and root.right is None:
			return True
		elif root.left is not None and root.right is not None:
			return self.dfs(root.left, tmp, side + [-1]) and self.dfs(root.right, tmp, side + [1])
		elif root.left is not None:
			return self.dfs(root.left, tmp, side + [-1])
		elif root.right is not None:
			return self.dfs(root.right, tmp, side + [1])

