class Solution {
public:
    int majorityElement(vector<int> &num) {
        map<int, int> hash;
        int n = (num.size() % 2 == 0) ? num.size() / 2 : num.size() / 2 + 1;
                for (auto i : num) {
            hash[i]++;
            if (hash[i] >= n) {
                return i;
            }
        }
    }
};