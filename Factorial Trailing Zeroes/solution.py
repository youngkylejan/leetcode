class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        ans = 0
        tmp = 1
        while n / math.pow(5, tmp) >= 1:
            ans = ans +  long(n / math.pow(5, tmp))
            tmp = tmp + 1
        return ans