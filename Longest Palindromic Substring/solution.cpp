class Solution {
public:
    string longestPalindrome(string s) {
                if (s.length() <= 0)
            return "";
        int len = s.length();
        bool dp[len][len];
                for (int i = 0; i < len; i++)
            for (int j = 0; j < len; j++) {
                dp[i][j] = i == j ? true : false;
            }
        string ans = s.substr(0,2);
        for (int i = 2; i < len; i++)
            for (int j = i - 1; j >= 0; j--)
                if (s[i] == s[j] && (i - j - 1 < 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                    ans = i - j + 1 >= ans.length() ? s.substr(j, i - j + 1) : ans;
                }
        return ans;
    }
};