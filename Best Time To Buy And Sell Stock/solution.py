class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		
		if len(prices) <= 0:
			return 0

		profit = 0
		min = prices[0]

		for price in prices:
			if price < min:
				min = price
			if price - min > profit:
				profit = price - min

		return profit