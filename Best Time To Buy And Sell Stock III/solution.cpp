class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        if (prices.size() == 0)
            return 0;

        std::vector<int> pre = std::vector<int>(prices.size(), 0);
        std::vector<int> end = std::vector<int>(prices.size(), 0);

        int minPre = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            minPre = min(minPre, prices[i]);
            if (prices[i] - minPre > pre[i - 1]) {
                pre[i] = prices[i] - minPre;
            } else {
                pre[i] = pre[i - 1];
            }
        }

        int maxEnd = prices[prices.size() - 1];
        for (int j = prices.size() - 2; j >= 0; j--) {
            maxEnd = max(maxEnd, prices[j]);
            if (maxEnd - prices[j] > end[j + 1]) {
                end[j] = maxEnd - prices[j];
            } else {
                end[j] = end[j + 1];
            }
        }

        int profit = 0;
        for (int i = 0; i < pre.size(); i++)
            profit = max(pre[i] + end[i], profit);

        return profit;
    }
};