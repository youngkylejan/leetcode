class Solution {
public:
    int log2(int x) {
        return log(x) / log(2);
    }

    int rangeBitwiseAnd(int m, int n) {

        if (m == n)
            return m;

        int diff = log2(n - m) + 1;
        m >>= diff;
        n >>= diff;
        return (m & n) << diff;

    }
};