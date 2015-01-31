/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cmath>

class Solution {
public:
    int height(TreeNode *node){

        if (!node) {
            return 0;
        }
        
        return max(height(node->left) + 1, height(node->right) + 1);
    }
    
    bool isBalanced(TreeNode *root) {
        
        if (!root) {
            return true;
        }
        
        if (abs(height(root->left) - height(root->right)) > 1) {
            return false;
        }
        
        return isBalanced(root->left) && isBalanced(root->right);
    }
};