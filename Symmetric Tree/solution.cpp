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
    bool traverse(TreeNode *left, TreeNode *right) {
        if (!left || !right) {
            return left == right;
        }
        return (left->val == right->val) && traverse(left->right, right->left) && traverse(left->left, 
right->right);
    }
    bool isSymmetric(TreeNode *root) {
        if (!root) {
            return true;
        }
        return traverse(root->left, root->right);
    }
};