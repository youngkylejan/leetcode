class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_map<int, int> m;
        int result = 0;
        for (auto item : num) {
            if (m.find(item) == m.end()) {
                int left = m.find(item - 1) != m.end() ? m[item - 1] : 0;
                int right = m.find(item + 1) != m.end() ? m[item + 1] : 0;
                int overall = left + right + 1;
                result = max(result, overall);
                m[item] = overall;
                m[item - left] = overall;
                m[item + right] = overall;
            }
        }
        return result;
    }
};