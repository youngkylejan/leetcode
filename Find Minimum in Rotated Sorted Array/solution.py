class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) <= 0:
            return None
        return self.process(num, 0, len(num) - 1)
    def process(self, num, start, end):
        mid = (start + end) / 2
        if start == end:
            return num[mid]
        if abs(start - end) == 1:
            return num[start] if num[start] < num[end] else num[end]
        if num[mid - 1] > num[mid] and num[mid + 1] > num[mid]:
            return num[mid]
        else:
            return min(self.process(num, mid + 1, end), self.process(num, start, mid - 1))