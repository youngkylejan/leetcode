class Solution {
public:
    int trailingZeroes(int n) {
        
        int ans = 0;
        int tmp = 1;

        while (n / pow(5, tmp) > 0) {
            ans += (n / pow(5, tmp));
            tmp++;
        }

        return ans;
    }
};