class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) <= 0:
            return 0
        minimum = [0] * len(ratings)
        minimum[0] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                minimum[i] = minimum[i - 1] + 1
            else:
                minimum[i] = 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and minimum[j] <= minimum[j + 1]:
                minimum[j] = minimum[j] + minimum[j + 1] - minimum[j] + 1
        ans = 0
        for item in minimum:
            ans = ans + item
        return ans
        