class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int>> results;
        vector<int> solution;

        backtracking(n, k, 1, results, solution);

        return results;
    }

    void backtracking(int n, int k, int start, vector<vector<int>>& results, vector<int>& solution) {

        if (solution.size() == k) {
            results.push_back(solution);
            return;
        }

        if (start > n || solution.size() > k)
            return;

        for (int i = start; i <= n; i++) {
            solution.push_back(i);
            backtracking(n, k, i + 1, results, solution);
            solution.pop_back();
        }
    }
};