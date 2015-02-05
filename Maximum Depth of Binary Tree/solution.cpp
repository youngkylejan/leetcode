/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 class Solution {
 public:
 	int dfs(TreeNode *root, int depth) {
 		if (!root) {
 			return depth;
 		}
 		return max(dfs(root->left, depth + 1), dfs(root->right, depth + 1));
 	}
 	int maxDepth(TreeNode *root) {
 		return dfs(root, 0);
 	}
 };