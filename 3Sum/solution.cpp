class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
    	
    	if (num.size() < 3)
    		return vector<vector<int>>();
    	
    	sort(num.begin(), num.end());
    
    	vector<vector<int>> results;
    	vector<int> solution;
    
    	for (int i = 0; i < num.size() - 1; i++) {
    		if (i > 0 && num[i] == num[i - 1])
    			continue;
    
    		int p = i + 1;
    		int q = num.size() - 1;
    
    		while (p < q) {
    
    			int value = num[i] + num[p] + num[q];
    
    			if (value == 0) {
    				solution.push_back(num[i]);
    				solution.push_back(num[p]);
    				solution.push_back(num[q]);
    				results.push_back(solution);
    				solution.clear();
    				p++;
    				while (p < q && num[p] == num[p-1])
    					p++;
    				q--;
    				while (p < q && num[q] == num[q+1])
    					q--;
    			} else if (value < 0) {
    				p++;
    			} else {
    				q--;
    			}
    		}
    	}
    
    	return results;
    }

};