class Solution {
public:
    int countPrimes(int n) {
        
        bool *v = new bool[n];
        for(int i = 0; i < n; i++)
            v[i] = false;

        int ans = 0;

        for (int i = 2; i < n; i += 1) {
            if (!v[i]) {
                ans++;

                for (int j = 2 * i; j < n; j += i)
                    v[j] = true;
            }
        }

        return ans;
    }
};