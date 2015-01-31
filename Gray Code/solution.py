class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        ans = [0, 1]
        strlist = ["0", "1"]
        m = 1
        while True:
            if m == n:
                break
            taillist = strlist[::-1]
            for i in range(0, len(strlist)):
                strlist[i] = "0" + strlist[i]
            for i in range(0, len(taillist)):
                taillist[i] = "1" + taillist[i]
                ans.append(int(taillist[i], 2))
            strlist = strlist + taillist
            m = m + 1
        return ans