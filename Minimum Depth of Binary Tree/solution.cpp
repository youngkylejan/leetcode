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
    int cal(TreeNode *root, int depth) {
        if (!root) {
            return depth;
        }
        if (root->left && root->right) {
            return min(cal(root->left, depth + 1), cal(root->right, depth + 1));
        } else if (root->left) {
            return cal(root->left, depth + 1);
        } else if (root->right) {
            return cal(root->right, depth + 1);
        } else {
            return depth;
        }
    }
    int minDepth(TreeNode *root) {
        if (!root) {
            return 0;
        }
        return cal(root, 1);    
    }
};