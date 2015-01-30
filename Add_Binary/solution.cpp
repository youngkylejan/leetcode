class Solution {
public:
    string addBinary(string a, string b) {
        int apos = a.length() - 1;
        int bpos = b.length() - 1;
        int adigit, bdigit, carry = 0;
        
        string result = "";
        while (apos >= 0 || bpos >= 0 || carry == 1) {
            if (apos >= 0) {
                adigit = a[apos--] == '1';
            }
            
            if (bpos >= 0) {
                bdigit = b[bpos--] == '1';
            }
            
            result = static_cast<char>(adigit ^ bdigit ^ carry + '0') + result;
            carry = adigit + bdigit + carry >= 2;
            adigit = bdigit = 0;
        }
        
        return result;
    }
};