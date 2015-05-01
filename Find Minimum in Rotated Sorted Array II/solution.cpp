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
    
        int i = minIndex - 1;
        for (int i = minIndex - 1; i >= start; i--)
            if (nums[i] != nums[minIndex])
                break;

        binarysearch(nums, start, i, ans);

        i = minIndex + 1;
        for (int i = minIndex + 1; i <= end; i++)
            if (nums[i] != nums[minIndex])
                break;

        binarysearch(nums, i, end, ans);
    }
};