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
        new_end = mid - 1
        while new_end - 1 > 0 and num[new_end] == num[mid]:
            new_end = new_end - 1
        new_start = mid + 1
        while new_start + 1 < len(num) and num[new_start] == num[mid]:
            new_start = new_start + 1
        if num[new_start] > num[mid] and num[new_end] > num[mid]:
            return num[mid]
                    return min(self.process(num, start, new_end), self.process(num, new_start, end))