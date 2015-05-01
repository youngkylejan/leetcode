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
    void flatten(TreeNode *root) {
        if (!root)
            return;
            
        TreeNode* newRoot = new TreeNode(0);
        preorder(root, newRoot);
        *root = *newRoot;
    }

    void preorder(TreeNode* root, TreeNode* newRoot) {

        newRoot->val = root->val;
        TreeNode* tmpNode = newRoot;
        
        if (root->left) {
            newRoot->right = new TreeNode(0);
            preorder(root->left, newRoot->right);
            while (tmpNode->right)
                tmpNode = tmpNode->right;
        }
        if (root->right) {
            tmpNode->right = new TreeNode(0);
            preorder(root->right, tmpNode->right);
        }

    }
};