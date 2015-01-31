class Solution {
public:
    void getNext(char* needle, int next[]) {
        int len = strlen(needle);
                next[0] = -1;
                int j = 0;
        int k = -1;
                while (j < len - 1) {
            if (k == -1 || needle[j] == needle[k]) {
                if (needle[++j] == needle[++k])
                    next[j] = next[k];
                else
                    next[j] = k;
            } else
                k = next[k];
        }
    }
        int strStr(char *haystack, char *needle) {
        int i = 0, j = 0;
            int len1 = strlen(haystack);
        int len2 = strlen(needle);
            int next[len2];
        getNext(needle, next);
                while (i < len1 && j < len2) {
            if (j == -1 || haystack[i] == needle[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }
                if (j == len2) {
            return i - j;
        } else {
            return -1;
        }
    }
};