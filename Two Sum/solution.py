class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hashs = {}
        index1 = 0
        index2 = 0
        for i in range(0, len(num)):
            if num[i] in hashs.keys():
                index1 = hashs[num[i]]
                index2 = i
                break
            if num[i] <= target:
                hashs[target - num[i]] = i
        return (index1 + 1, index2 + 1)