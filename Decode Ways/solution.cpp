class Solution {
public:
    int numDecodings(string s) {
        
        if (s[0] == '0' || s == "")
            return 0;
            
        int* dp = new int[s.length() + 1];

        for (int i = 0; i < s.length() + 1; i++)
            dp[i] = 0;

        dp[0] = 1;
        dp[1] = 1;

        int j = 2;

        for (int i = 1; i < s.length(); i++) {
            
            int cur = (s[i - 1] - '0') * 10 + s[i] - '0';

            if (s[i] == '0' && (cur > 26 || cur == 0))
                return 0;
            else if (cur < 26 && s[i] == '0')
                dp[j] = dp[j - 2];
            else if (s[i - 1] == '0')
                dp[j] = dp[j - 1];
            else if (cur > 26)
                dp[j] = dp[j - 1];
            else
                dp[j] = dp[j - 1] + dp[j - 2];

            j += 1;
        }

        return dp[s.length()];
    }
};