# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		if root is None:
			return []

		stack = []
		pre = None
		stack.append(root)

		ans = []
		while len(stack) > 0:
			cur = stack[len(stack) - 1]

			if (cur.left is None and cur.right is None) or (pre is not None and (pre == cur.left or pre == cur.right)):
				ans.append(stack.pop().val)
				pre = cur
			else:
				if cur.right is not None:
					stack.append(cur.right)
				if cur.left is not None:
					stack.append(cur.left)

		return ans        