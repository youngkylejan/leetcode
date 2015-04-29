class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int>> results;
        vector<int> solution;

        sort(candidates.begin(), candidates.end());
        backtracking(candidates, results, solution, target, 0, 0);
        return results;
    }

    void backtracking(vector<int> candidates, vector<vector<int>>& results, vector<int>& solution, int target, int start, int sum) {

        if (start >= candidates.size() || sum > target)
            return;

        if (sum == target) {
            results.push_back(std::vector<int>(solution.begin(), solution.end()));
            return;
        }

        solution.push_back(candidates[start]);
        backtracking(candidates, results, solution, target, start, sum + candidates[start]);
        solution.pop_back();
        backtracking(candidates, results, solution, target, start + 1, sum);
    }
};