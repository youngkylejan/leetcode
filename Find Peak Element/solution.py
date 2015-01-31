class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) <= 0:
            return None
        if len(num) == 1:
            return 0
        if len(num) == 2:
            return 0 if num[0] > num[1] else 1
        ans = []
        flag = [False] * len(num)
        flag[0] = True
        ans.append(0)
        for i in range(1, len(num)):
            if num[i] >= num[i - 1] and flag[i - 1] == True:
                ans.pop()
                flag[i - 1] = False
                flag[i] = True
                ans.append(i)
            elif num[i] >= num[i - 1] and flag[i - 1] == False:
                flag[i] = True
                ans.append(i)
            elif flag[i - 1] == True:
                break
        return ans[0]