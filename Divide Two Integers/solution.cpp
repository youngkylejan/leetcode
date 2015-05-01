class Solution {
public:
    int divide(int dividend, int divisor) {
        
        int flag = (dividend > 0) ^ (divisor > 0) ? -1 : 1;

        long a = labs(dividend);
        long b = labs(divisor);

        long ans = 0;

        while(a >= b) {
            int i = 0;
            while(a >= b<<i) {
                a -= b<<i;
                ans += 1<<i;
                i++;
            }
        }

        ans = (flag == 1) ? ans : -ans;

        if (ans > 0)
            return (ans > numeric_limits<int>::max()) ? numeric_limits<int>::max() : ans;
        else if (ans < 0)
            return (ans < numeric_limits<int>::min()) ? numeric_limits<int>::min() : ans;

        return ans;
    }
};