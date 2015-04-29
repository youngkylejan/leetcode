class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        
        if (!root)
            return vector<int>();

        std::stack<TreeNode*> s;
        std::vector<int> ans;
        s.push(root);

        while (s.size() > 0) {
            auto cur = s.top();
            ans.push_back(cur->val);
            s.pop();

            if (cur->right)
                s.push(cur->right);
            if (cur->left)
                s.push(cur->left);
        }

        return ans;
    }
};