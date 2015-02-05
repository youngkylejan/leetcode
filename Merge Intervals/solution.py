# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):

        if len(intervals) <= 0:
            return []

        l = sorted(intervals, cmp=self.compare)

        stack = []
        stack.append(l[0])

        for i in range(1, len(l)):
            previous = stack[len(stack) - 1]

            if l[i].start >= previous.start and l[i].end <= previous.end:
                continue
            elif l[i].start >= previous.start and l[i].start <= previous.end and l[i].end > previous.end:
                stack.pop()
                stack.append(Interval(previous.start, l[i].end))
            else:
                stack.append(l[i])

        return stack

    def compare(self, a, b):
        return a.start - b.start