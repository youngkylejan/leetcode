class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        backtracking(res, n, "", 0, 0);
        return res;
    }

    void backtracking(vector<string>& res, int n, string str, int left, int right) {
        if (left < right)
            return;

        if (left > n)
            return;

        if (left == n && right == n) {
            res.push_back(str);
            return;
        }

        str += "(";
        backtracking(res, n, str, left + 1, right);
        str.pop_back();
        str += ")";
        backtracking(res, n, str, left, right + 1);
        str.pop_back();
    }
};