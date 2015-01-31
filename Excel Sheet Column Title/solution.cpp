class Solution {
public:
    string convertToTitle(int n) {
                string ans;
                while (n) {
            int remainder = n % 26;
            n = n / 26;
                        if (remainder == 0) {
                ans += 'Z';
                n--;
            } else {
                ans += ('A' + remainder - 1);
            }
        }
                int len = ans.length();
        for (int i = 0; i <= len / 2 - 1; i++) {
            int temp = ans[i];
            ans[i] = ans[len - i - 1];
            ans[len - i - 1] = temp;
        }
                return ans;
    }
};