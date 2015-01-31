class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.pow(1/x, -n)
        elif n % 2 == 0:
            return self.pow(x * x, n / 2)
        else:
            return self.pow(x * x, (n - 1) / 2) * x