class Solution {
public:
    int candy(vector<int>& ratings) {
        
        std::vector<int> tmp = std::vector<int>(ratings.size(), 0);
        tmp[0] = 1;

        for (int i = 1; i < ratings.size(); i++) {
            if (ratings[i] > ratings[i - 1])
                tmp[i] = tmp[i - 1] + 1;
            else
                tmp[i] = 1;
        }

        for (int i = ratings.size() - 2; i >= 0; i--) {
            if (tmp[i] <= tmp[i + 1] && ratings[i] > ratings[i + 1])
                tmp[i] += tmp[i + 1] - tmp[i] + 1;
        }

        int ans = 0;
        for (auto x : tmp)
            ans += x;
        return ans;
    }
};