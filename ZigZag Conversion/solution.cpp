class Solution {
public:
    string convert(string s, int nRows) {
                if (nRows == 1)
            return s;
                string ans = "";
                int len = s.length();
        int smart = 2 * nRows - 2;
                for (int i = 0; i < len; i += smart) {
            ans += s[i];
        }
                int k = nRows - 1;
        for (int i = 1; i < k; i++) {
            for (int j = 0; j - i < len; j += smart) {
                if (j - i >= 0) {
                    ans += s[j - i];
                }
                if (j + i < len) {
                    ans += s[j + i];
                }
            }
        }
                for (int i = k; i < len; i += smart) {
            ans += s[i];
        }
                return ans;
    }
};