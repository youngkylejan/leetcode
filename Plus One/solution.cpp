class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int plus = 1;
        int len = digits.size();
                for (int i = len - 1; i >= 0; i--) {
            if (digits[i] + 1 > 9) {
                digits[i] = 0;
                plus = 1;
            } else {
                digits[i] += 1;
                plus = 0;
                break;
            }
        }
                if (plus == 1) {
            digits.insert(digits.begin(), 1, 1);
        }
                return digits;
    }
};