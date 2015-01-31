class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size() <= 0) {
        return "";
    }
        string ans = "";
        for (int i = 0; i < strs[0].length(); i++) {
        char c = strs[0][i];
                bool flag = true;
        for (int j = 1; j < strs.size(); j++) {
            if (strs[j].size() <= 0) {
                flag = false;
                break;
            }
                        char nextC = strs[j][i];
                        if (nextC != c) {
                flag = false;
                break;
            }
        }
                if (flag) {
            ans.push_back(c);
        } else {
            break;
        }
    }
        return ans;
}
};