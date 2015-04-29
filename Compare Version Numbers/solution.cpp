class Solution {
public:
    int compareVersion(string version1, string version2) {
        
        int l1 = version1.length();
        int l2 = version2.length();
        int i = 0, j = 0;

        int num1 = 0, num2 = 0;

        while (i < l1 || j < l2) {

            while (i < l1 && version1[i] != '.') {
                num1 = num1 * 10 + version1[i] - '0';
                i++;
            }

            while (j < l2 && version2[j] != '.') {
                num2 = num2 * 10 + version2[j] - '0';
                j++;
            }

            if (num1 > num2)
                return 1;
            else if (num1 < num2)
                return -1;

            num1 = 0;
            num2 = 0;
            i++;
            j++;
        }

        return 0;
    }
};