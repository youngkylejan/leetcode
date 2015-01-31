class Solution {
public:
    bool isPalindrome(int x) {
        int min = 0, max = x;
                if (x < 0) {
            return false;
        }
                while (x) {
            min = min * 10 + x % 10;
            x /= 10;
        }
                return min == max;
    }
};