class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) <= 1:
            return 0
        maxNum = num[0]
        minNum = num[0]
        for item in num:
            maxNum = max(item, maxNum)
            minNum = min(item, minNum)
        interval = (int)(math.ceil(float((maxNum - minNum)) / (len(num) - 1)))
        backetMin = [maxNum + 1] * len(num)
        backetMax = [minNum - 1] * len(num)
        for item in num:
            if item == minNum or item == maxNum:
                continue
            index = (item - minNum) / interval
            backetMin[index] = min(item, backetMin[index])
            backetMax[index] = max(item, backetMax[index])
        gap = 0
        previous = minNum
        for i in range(0, len(backetMin)):
            if backetMin[i] == maxNum + 1 and backetMax[i] == minNum - 1:
                continue
            gap = max(backetMin[i] - previous, backetMax[i] - backetMin[i], gap)
            previous = backetMax[i]
        gap = max(gap, maxNum - previous)
        return gap