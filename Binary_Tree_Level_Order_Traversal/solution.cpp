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
	void DFS(TreeNode *root, int depth, vector<vector<int>>& result) {
		if (!root) {
			return;
		}

		if (depth == result.size()) {
			result.push_back(vector<int>());
		}

		result[depth].push_back(root->val);
		DFS(root->left, depth + 1, result);
		DFS(root->right, depth + 1, result);
	}

    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int>> result;
        DFS(root, 0, result);
        return result;
    }
};