class Solution {
public:
    int titleToNumber(string s) {
        
        unordered_map<char, int> hashs;

        for (int i = 1; i <= 26; i++)
            hashs['A' + i - 1] = i;

        int ans = 0;
        int j = 0;

        for (int i = s.length() - 1; i >= 0; i--, j++) {
            ans += hashs[s[i]] * pow(26, j);
        }

        return ans;
    }
};