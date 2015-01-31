class Solution {
public:
    bool isValid(string s) {
                stack<char> sta;
        map<char, char> hash;
                hash['('] = ')';
        hash['{'] = '}';
        hash['['] = ']';
                int flag = 0;
        int len = s.length();
        for (int i = 0; i < len; i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                sta.push(s[i]);
                flag++;
            } else if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
                if (sta.empty()) {
                    return false;
                } else if (hash[sta.top()] != s[i]) {
                    return false;
                }
                flag--;
                sta.pop();
            }
        }
                return flag == 0 ? true : false;
    }
};