class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int index = -1;
        binarysearch(nums, 0, nums.size() - 1, index);
        return index;
    }

    void binarysearch(vector<int>& nums, int start, int end, int& index) {
        if (index != -1)
            return;

        if (start > end)
            return;

        int minIndex = (start + end) / 2;

        if (minIndex - 1 < 0 && (minIndex + 1 >= nums.size() || nums[minIndex] > nums[minIndex + 1])) {
            index = minIndex;
            return;
        }

        if (minIndex + 1 >= nums.size() && (minIndex - 1 < 0 || nums[minIndex] > nums[minIndex - 1])) {
            index = minIndex;
            return;
        }

        if (nums[minIndex] > nums[minIndex - 1] && nums[minIndex] > nums[minIndex + 1]) {
            index = minIndex;
            return;
        }

        binarysearch(nums, start, minIndex - 1, index);
        binarysearch(nums, minIndex + 1, end, index);
    }
};