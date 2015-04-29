class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        std::vector<std::vector<int>> rows;
        dfs(root, rows, 0);

        for (int i = 0; i < rows.size(); i++) {
            if (i % 2)
                rows[i] = std::vector<int>(rows[i].rbegin(), rows[i].rend());
        }

        return rows;
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