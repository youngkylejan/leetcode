class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 0)
            return vector<int>(1, 0);

        vector<int> res = vector<int>();
        backtracking(res, n);
        return res;
    }

    void backtracking(vector<int>& res, int n) {
        if (n == 1) {
            res.push_back(0);
            res.push_back(1);
            return;
        }

        backtracking(res, n - 1);

        for (int i = res.size() - 1; i >= 0; i--) {
            res.push_back(res[i] | (1 << n - 1));
        }
    }
};