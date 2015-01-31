class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) <= 0:
            return -1
        start = len(gas) - 1
        end = 0
        sum = gas[start] - cost[start]
        while start > end:
            if sum >= 0:
                sum += gas[end] - cost[end]
                end = end + 1
            else:
                start = start - 1
                sum += gas[start] - cost[start]
        return start if sum >= 0 else -1