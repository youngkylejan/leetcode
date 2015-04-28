
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BSTIterator {
private:
    std::vector<int> numbers;
    int index;

    void inorder(TreeNode *root) {
        if (root != NULL) {
            inorder(root->left);
            numbers.push_back(root->val);
            inorder(root->right);
        }
    }

public:
    BSTIterator(TreeNode *root) {
        index = 0;
        inorder(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        if (index < numbers.size())
            return true;
        return false;
    }

    /** @return the next smallest number */
    int next() {
        index += 1;
        return numbers[index - 1];
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */