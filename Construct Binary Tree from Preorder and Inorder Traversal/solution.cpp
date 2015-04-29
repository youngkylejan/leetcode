class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return build(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }

    TreeNode *build(vector<int>& preorder, vector<int>& inorder, int ps, int pe, int is, int ie) {

        if (ps > pe || is > ie)
            return NULL;

        TreeNode* root = new TreeNode(preorder[ps]);

        int i = is;
        for (; i <= ie; i++)
            if (inorder[i] == root->val)
                break;
        int l = i - is;

        root->left = build(preorder, inorder, ps + 1, ps + l, is, is + l - 1);
        root->right = build(preorder, inorder, ps + l + 1, pe, is + l + 1, ie);

        return root;
    }
};