class Solution {
public:
    void backtrace(vector<vector<string>>& result, vector<string> v, int row, int n) {
        if (row == n) {
            result.push_back(vector<string>(v));
            return;
        }
        for (int j = 0; j < n; j++) {
            int a = row, p = j, q = j;
            bool isSafe = true;
            while (a >= 0) {
                if (a != row && v[a][j] == 'Q') {
                    isSafe = false;
                    break;
                }
                a--;
            }
                        if (!isSafe) {
                continue;
            }
                        a = row;
            while (a >= 0 && p >= 0) {
                if (a != row && p != j && v[a][p] == 'Q') {
                    isSafe = false;
                    break;
                }
                a--;
                p--;
            }
                        if (!isSafe) {
                continue;
            }
                        a = row;
            while (a >= 0 && q < n) {
                if (a != row && q != j && v[a][q] == 'Q') {
                    isSafe = false;
                    break;
                }
                a--;
                q++;
            }
                        if (!isSafe) {
                continue;
            }
                        v[row][j] = 'Q';
            backtrace(result, v, row + 1, n);
            v[row][j] = '.';
        }
    }
    vector<vector<string> > solveNQueens(int n) {
                vector<string> v;
                string line = "";
        for (int i = 0; i < n; i++)
            line = line + ".";
        for (int i = 0; i < n; i++)
            v.push_back(line);
        vector<vector<string>> result;
                backtrace(result, v, 0, n);
        return result;
    }
};