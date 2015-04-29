class Solution {
public:
    TreeNode *build(vector<int>& inorder, int is, int ie, vector<int>& postorder, int ps, int pe) {
    
        if (is > ie || ps > pe)
            return NULL;
    
        TreeNode* root = new TreeNode(postorder[pe]);
    
        int i = is;
        for (; i <= ie; i++)
            if (inorder[i] == root->val)
                break;
        int l = i - is;
    
        root->left = build(inorder, is, is + l - 1, postorder, ps, ps + l - 1);
        root->right = build(inorder, is + l + 1, ie, postorder, ps + l, pe - 1);
    
        return root;
    }
    
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
    
        if (inorder.size() <= 0)
            return NULL;
    
        return build(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
};