class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        ans = []
        ans.append([1])
        count = 0
        while numRows > 1:
            nextRow = []
            nextRow.append(1)
            for index in range(len(ans[count])):
                if index + 1 > len(ans[count]) - 1:
                    break
            nextRow.append(ans[count][index] + ans[count][index + 1])
            nextRow.append(1)
            ans.append(nextRow)
            numRows = numRows - 1
            count = count + 1
        return ans        