class Solution {
public:
    vector<int> rightSideView(TreeNode *root) {
        std::vector<int> ans;
        std::vector<std::vector<int>> rows;
        dfs(root, rows, 0);

        for (auto row : rows)
            ans.push_back(row[row.size() - 1]);

        return ans;
    }

    void dfs(TreeNode* root, std::vector<std::vector<int>>& v, int depth) {
        if (!root)
            return;

        if (depth == v.size())
            v.push_back(std::vector<int>());
        
        v[depth].push_back(root->val);

        dfs(root->left, v, depth + 1);
        dfs(root->right, v, depth + 1);
    }
};