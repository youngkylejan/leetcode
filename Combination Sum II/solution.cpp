class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
        set<vector<int>> results;
        vector<int> solution;

        sort(candidates.begin(), candidates.end());
        backtracking(candidates, results, solution, target, 0, 0);
        return vector<vector<int>>(results.begin(), results.end());
    }

    void backtracking(vector<int> candidates, set<vector<int>>& results, vector<int>& solution, int target, int start, int sum) {
        if (start > candidates.size() || sum > target)
            return;

        if (sum == target) {
            results.insert(solution);
            return;
        }

        solution.push_back(candidates[start]);
        backtracking(candidates, results, solution, target, start + 1, sum + candidates[start]);
        solution.pop_back();

        if (sum + candidates[start] > target)
            return;

        backtracking(candidates, results, solution, target, start + 1, sum);
    }
};