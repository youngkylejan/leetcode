class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        if (!root)
            return vector<int>();
        
        std::stack<TreeNode*> s;
        s.push(root);
        TreeNode* child;
        std::vector<int> ans;

        while (s.size() > 0) {
            TreeNode* cur = s.top();

            if ((!cur->left && !cur->right) || (child && (cur->left == child or cur->right == child))) {
                ans.push_back(cur->val);
                s.pop();
                child = cur;
            } else {
                if (cur->right)
                    s.push(cur->right);
                if (cur->left)
                    s.push(cur->left);
            }
        }

        return ans;
    }
};