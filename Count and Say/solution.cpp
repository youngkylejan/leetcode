class Solution {
public:
    string nextStr(string str) {

        string ans = "";
        int len = str.length();
        char temp = str[0];
        int count = 1;
        for (int i = 1; i < len; i++) {
            if (str[i] == temp) {
                count++;
            } else {
                ans += to_string(count) + temp;
                temp = str[i];
                count = 1;
            }
        }
        ans += to_string(count) + temp;
        return ans;
    }
    
    string countAndSay(int n) {
        string ans = "1";
        while (--n) {
            ans = nextStr(ans);
        }
        return ans;
    }
};