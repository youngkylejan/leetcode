struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    int ans;

public:
    Solution() {
        ans = std::numeric_limits<int>::min();
    }

    int maxPathSum(TreeNode *root) {
        getMax(root);
        return ans;
    }

    int getMax(TreeNode *root) {
        if (!root)
            return 0;

        int leftValue = getMax(root->left);
        int rightValue = getMax(root->right);

        int value = root->val;
        if (leftValue > 0)
            value += leftValue;
        if (rightValue > 0)
            value += rightValue;

        ans = max(ans, value);

        if (leftValue > rightValue && leftValue > 0)
            return root->val + leftValue;

        if (rightValue > leftValue && rightValue > 0)
            return root->val + rightValue;

        return root->val;
    }
};