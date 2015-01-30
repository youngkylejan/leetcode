class Solution:
	# @return a list of tree node
	def generateTrees(self, n):
		return self.dfs(1, n)

	def dfs(self, start, end):

		result = []
		if (start > end):
			result.append(None)
			return result

		for rootVal in range(start, end + 1):
			left = self.dfs(start, rootVal - 1)
			right = self.dfs(rootVal + 1, end)

			for i in range(0, len(left)):
				for j in range(0, len(right)):
					root = TreeNode(rootVal)
					root.left = left[i]
					root.right = right[j]
					result.append(root)

		return result
