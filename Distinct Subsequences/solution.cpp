class Solution {
public:
    int numDistinct(string s, string t) {
        
        vector<vector<int>> dp = vector<vector<int>>(t.length() + 1, vector<int>(s.length() + 1, 0));

        for (int i = 0; i <= s.length(); i++)
            dp[0][i] = 1;

        for (int i = 1; i <= t.length(); i++)
            for (int j = 1; j <= s.length(); j++) {
                if (s[j - 1] != t[i - 1])
                    dp[i][j] = dp[i][j - 1];
                else
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
            }

        return dp[t.length()][s.length()];
    }
};