class Solution {
public:
    int findMin(vector<int>& nums) {
        
        int start = 0, end = nums.size() - 1;
        int ans = numeric_limits<int>::max();

        binarysearch(nums, 0, nums.size() - 1, ans);
        return ans;
    }

    void binarysearch(vector<int>& nums, int start, int end, int& ans) {

        if (start > end)
            return;

        int minIndex = (start + end) / 2;
        ans = min(ans, nums[minIndex]);

        binarysearch(nums, start, minIndex - 1, ans);
        binarysearch(nums, minIndex + 1, end, ans);
    }
};