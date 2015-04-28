class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        
        if (num.size() < 4)
            return vector<vector<int>>();
    
        sort(num.begin(), num.end());
    
        vector<vector<int>> results;
    
        for (size_t i = 0; i < num.size() - 3; i++) {
            if (i > 0 && num[i] == num[i - 1])
                continue;
    
            for (size_t j = num.size() - 1; j > 0; j--) {
                if (j < num.size() - 1 && num[j] == num[j + 1])
                    continue;
                
                int p = i + 1;
                int q = j - 1;
    
                while (p < q) {
                    int value = num[i] + num[p] + num[q] + num[j] - target;
    
                    if (value == 0) {
                        vector<int> tmp;
                        tmp.push_back(num[i]);
                        tmp.push_back(num[p]);
                        tmp.push_back(num[q]);
                        tmp.push_back(num[j]);
                        results.push_back(tmp);
    
                        p++;
                        while (p < q && num[p] == num[p - 1]) p++;
    
                        q--;
                        while (p < q && num[q] == num[q + 1]) q--;
    
                    } else if (value < 0) {
                        p++;
                    } else {
                        q--;
                    }
                }
            }
        }
    
        return results;
    }
};