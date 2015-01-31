class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
    	vector<vector<int>> results;

    	if (num.size() < 4) {
    		return results;
    	}

    	sort(num.begin(), num.end());

    	unordered_map<long long, vector<pair<int, int>>> hash;

    	for (int i = 0; i < num.size(); i++) {
    		for (int j = i + 1; j < num.size(); j++) {
    			if (j > i + 1 && num[j] == num[j - 1]) {
    				continue;
    			}
    			hash[num[i] + num[j]].push_back(pair<int, int>(i, j));
    		}
    	}

    	set<vector<int>> setHash;
    	for (int p = 0; p < num.size() - 3; p++) {
    		if (p > 0 && num[p] == num[p - 1]) {
    			continue;
    		}
    		for (int q = p + 1; q < num.size(); q++) {
    			if (q > p + 1 && num[q] == num[q - 1]) {
    				continue;
    			}
    			long long twoSum = num[p] + num[q];

    			long long theta = (long long)target - twoSum;

    			if (hash[theta].size()) {
    				for (int k = 0; k < hash[theta].size(); k++) {
    					int thirdIndex = hash[theta][k].first;
    					int forthIndex = hash[theta][k].second;

    					if (thirdIndex > p && thirdIndex > q) {
    						vector<int> tmp;
    						tmp.push_back(num[p]);
    						tmp.push_back(num[q]);
    						tmp.push_back(num[thirdIndex]);
    						tmp.push_back(num[forthIndex]);

    						if (setHash.find(tmp) == setHash.end()) {
    							setHash.insert(tmp);
    							results.push_back(tmp);
    						}
    					}
    				}
    			}
    		}
    	}

    	return results;
    }
};