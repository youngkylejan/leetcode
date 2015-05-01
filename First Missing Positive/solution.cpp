class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (nums.size() <= 0)
            return 1;

        bool* bucket = new bool[nums.size() + 2];

        for (int i = 0; i <= nums.size() + 1; i++)
            bucket[i] = false;

        for (auto x : nums)
            if (x > 0)
                bucket[x] = true;

        for (int i = 1; i <= nums.size() + 1; i++)
            if (!bucket[i])
                return i;
    }
};