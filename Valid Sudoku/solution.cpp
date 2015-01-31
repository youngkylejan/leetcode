class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        map<char, int> hash;
                for (int i = 0; i < 9; i++) {
            hash.clear();
            for (int j = 0; j < 9; j++) {
                hash[board[i][j]]++;
                if (board[i][j] != '.' && hash[board[i][j]] >= 2) {
                    return false;
                }
            }
        }
                for (int i = 0; i < 9; i++) {
            hash.clear();
            for (int j = 0; j < 9; j++) {
                hash[board[j][i]]++;
                if (board[j][i] != '.' && hash[board[j][i]] >= 2) {
                    return false;
                }
            }
        }
                for (int m=0;m<9;m+=3) {  
            for (int n=0;n<9;n+=3) {  
                hash.clear();  
                for (int i=m;i<m+3;i++) {  
                    for (int j=n;j<n+3;j++) {  
                        hash[board[i][j]]++;  
                        if (hash[board[i][j]]>1&&board[i][j]!='.') {  
                            return false;  
                        }  
                    }  
                }  
            }  
        }
                return true;
    }
};