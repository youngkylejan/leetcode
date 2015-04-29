class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return build(num, 0, num.size());
    }

    TreeNode *build(vector<int>& num, int start, int end) {

        if (start >= end)
            return NULL;

        int minIndex = (start + end) / 2;
        TreeNode* root = new TreeNode(num[minIndex]);

        root->left = build(num, start, minIndex);
        root->right = build(num, minIndex + 1, end);

        return root;
    }
};