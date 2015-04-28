class Solution {
public:
	int maxProfit(vector<int>& prices) {
		
		if (prices.size() == 0)
			return 0;

		int profit = 0;
		int min_price = prices[0];

		for (auto price : prices) {
			if (price < min_price)
				min_price = price;
			if (price - min_price > profit)
				profit = price - min_price;
		}

		return profit;
	}
};