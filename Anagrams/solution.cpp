class Solution {
public:
	vector<string> anagrams(vector<string>& strs) {
		
		std::unordered_map<std::string, std::vector<std::string>> hashs;

		for (auto str : strs) {
			std::string tmp = str;
			sort(tmp.begin(), tmp.end());
			if (hashs.find(tmp) == hashs.end())
				hashs[tmp].push_back(str);
			else
				hashs[tmp].push_back(str);
		}

		std::vector<string> ans;

		for (auto item : hashs) {
			if (item.second.size() >= 2) {
				for (auto str : item.second)
					ans.push_back(str);
			}
		}

		return ans;
	}
};