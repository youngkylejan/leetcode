class Solution {
public:
int atoi(const char *str) {
    string s(str);
    int len = s.length();
        bool flag = false;
    bool outFlag = false;
    long long ans = 0;
        int start = 0;
    bool orientation = true;
    bool hasNum = false;
        for (int i = 0; i < len; i++) {
        if (s[i] == ' ') {
            continue;
        } else if (s[i] == '+' || s[i] == '-') {
            start = i + 1;
            orientation = s[i] == '+' ? true : false;
            break;
        } else {
            start = i;
            orientation = true;
            break;
        }
    }
        for (int i = start; i < len; i++) {
                if (!hasNum && !(s[i] - '0' >= 0 && s[i] - '0' <= 9)) {
            flag = false;
            break;
        }
                if (hasNum && s[i] == ' ') {
            break;
        } else if (hasNum && !(s[i] - '0' >= 0 && s[i] - '0' <= 9)) {
            break;
        }
                if (!flag && !hasNum && (s[i] - '0' >= 0 && s[i] - '0' <= 9)) {
            flag = true;
            hasNum = true;
        }
                ans = ans * 10 + s[i] - '0';
                if (ans > INT_MAX || ans < INT_MIN) {
            outFlag = true;
            break;
        }
    }
        if (!flag) {
        return 0;
    }
        if (outFlag) {
        return orientation == true ? INT_MAX : INT_MIN;
    }
        return orientation == true ? ans : -ans;
}
};