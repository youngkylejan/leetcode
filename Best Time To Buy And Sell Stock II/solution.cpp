class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        if (prices.size() == 0)
            return 0;

        int profit = 0;
        int buyPrice = prices[0];

        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] - buyPrice > 0) {
                profit += prices[i] - buyPrice;
                buyPrice = prices[i];
            } else if (prices[i] - buyPrice < 0) {
                buyPrice = prices[i];
            }
        }

        return profit;
    }
};