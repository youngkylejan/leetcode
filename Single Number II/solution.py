class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = twos = threes = 0
        for i in range(0, len(A)):
            twos = twos | (ones & A[i])
            ones = ones ^ A[i]
            threes = ~(ones & twos)
            ones = ones & threes
            twos = twos & threes
        return ones