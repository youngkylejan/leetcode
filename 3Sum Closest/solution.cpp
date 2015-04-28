class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
    	
    	if (num.size() < 3)
    		return 0;
    	
    	sort(num.begin(), num.end());
    
    	int solution = 0;
    	int delta = std::numeric_limits<int>::max();
    
    	for (int i = 0; i < num.size() - 1; i++) {
    		if (i > 0 && num[i] == num[i - 1])
    			continue;
    
    		int p = i + 1;
    		int q = num.size() - 1;
    
    		while (p < q) {
    
    			int curDelta = num[i] + num[p] + num[q] - target;
    
    			if (curDelta == 0) {
    				return target;
    			} else if (curDelta < 0) {
    				if (abs(curDelta) < abs(delta)) {
    					delta = curDelta;
    					solution = curDelta + target;
    				}
    				p++;
    			} else {
    				if (abs(curDelta) < abs(delta)) {
    					delta = curDelta;
    					solution = curDelta + target;
    				}
    				q--;
    			}
    		}
    	}
    
    	return solution;
    }
};