class Solution {
public:
    bool isHappy(int n) {

        unordered_set<int> visit;

        while (visit.find(n) == visit.end()) {
            
            visit.insert(n);

            int tmp = n;
            int newn = 0;
            while (tmp) {
                newn += pow(tmp % 10, 2);
                tmp /= 10;
            }
            n = newn;

            if (n == 1)
                return true;
        }

        return false;
    }
};