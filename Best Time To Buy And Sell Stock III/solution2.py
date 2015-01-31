class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	if len(prices) < 2:
    		return 0

    	pre = [0] * len(prices)
    	end = [0] * len(prices)

    	minPre = prices[0]
    	for i in range(1, len(prices)):
    		minPre = min(minPre, prices[i])
    		pre[i] = prices[i] - minPre if prices[i] - minPre > pre[i - 1] else pre[i - 1]

    	maxEnd = prices[len(prices) - 1]
    	for j in range(len(prices) - 2, -1, -1):
    		maxEnd = max(maxEnd, prices[j])
    		end[j] = maxEnd - prices[j] if maxEnd - prices[j] > end[j + 1] else end[j + 1]

    	Profit = 0
    	for k in range(0, len(pre)):
    		Profit = max(Profit, pre[k] + end[k])

    	return Profit
