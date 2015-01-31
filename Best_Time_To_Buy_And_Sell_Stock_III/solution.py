class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	if len(prices) < 2:
    		return 0

    	current = [0] * 3
    	whole = [0] * 3

    	for i in range(0, len(prices) - 1):
    		diff = prices[i + 1] - prices[i]

    		for j in range(2, 0, -1):
    			current[j] = max(whole[j - 1] + diff if diff > 0 else 0, current[j] + diff)
    			whole[j] = max(current[j], whole[j])

    	return whole[2]
