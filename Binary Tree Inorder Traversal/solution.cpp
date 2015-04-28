
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {

        if (!root)
            return vector<int>();

        std::stack<int> s;
        std::vector<int> ans;
        TreeNode* p = root;

        while (p != NULL || s.size() > 0) {    
            if (p) {
                s.push_back(p);
                p = p->left;
            } else {
                tmp = s.pop();
                ans.push_back(tmp->val);
                p = tmp->right;
            }
        }

        return ans;
    }
};