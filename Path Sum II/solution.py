# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        result = []
        ans = []
        self.dfs(root, sum, result, ans, 0)
        return result
    def dfs(self, root, sum, result, ans, num):
        num = num + root.val
        if num == sum and root.left is None and root.right is None:
            result.append(ans[::1] + [root.val])
            return
        if root.left is not None:
            self.dfs(root.left, sum, result, ans[::1] + [root.val], num)
        if root.right is not None:
            self.dfs(root.right, sum, result, ans[::1] + [root.val], num)