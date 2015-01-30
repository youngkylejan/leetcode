class Solution:
	# @return an integer
	def numTrees(self, n):

		dp = [0] * (n + 2)
		dp[0] = 1
		dp[1] = 1
		dp[2] = 2

		for i in range(3, n + 1):
			for j in range(1, i + 1):
				dp[i] = dp[i] + dp[j - 1] * dp[i - j]

		return dp[n]	
