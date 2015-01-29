class Solution:
	# @return a boolean
	def isScramble(self, s1, s2):
		
		if len(s1) != len(s2):
			return True

		n = len(s1)
		dp = [[[False for l in xrange(n + 1)] for j in xrange(n)] for i in xrange(n)]
		
		for l in xrange(1, n + 1):
			for i in xrange(0, n - l + 1):
				for j in xrange(0, n - l + 1):
					if l == 1:
						dp[i][j][l] = s1[i] == s2[j]
					for k in xrange(1, l):
						if (dp[i][j][k] and dp[i+k][j+k][l-k]) or (dp[i][j+l-k][k] and dp[i+k][j][l-k]):
							dp[i][j][l] = True
							break

		return dp[n][0][0]