# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) <= 0:
            return [newInterval]
        result = []
        begin = -1
        end = -1
        s = newInterval.start
        e = newInterval.end
        new = Interval(s, e)
        for i in range(0, len(intervals)):
            if begin == -1 or end == -1:
                if self.process(intervals[i], s) == 0 and self.process(intervals[i], e) == 0:
                    result.append(intervals[i])
                    begin = end = i
                    continue
                if self.process(intervals[i], s) > 0 and self.process(intervals[i], e) > 0:
                    result.append(intervals[i])
                    continue
                if begin == -1 and self.process(intervals[i], s) < 0:
                    begin = i
                    new.start = s
                elif begin == -1 and self.process(intervals[i], s) == 0:
                    begin = i
                    new.start = intervals[i].start
                if self.process(intervals[i], e) == 0:
                    end =  i
                    new.end = intervals[i].end
                    result.append(new)
                    continue
                elif self.process(intervals[i], e) < 0:
                    end = i
                    new.end = e
                    result.append(new)
                    result.append(intervals[i])
                elif self.process(intervals[i], e) > 0 and i + 1 < len(intervals) and self.process
(intervals[i+1], e) < -1:
                    end = i
                    new.end = e
                    result.append(new)
                    continue
                elif self.process(intervals[i], e) > 0 and i + 1 == len(intervals):
                    end = i + 1
                    new.end = e
                    result.append(new)
                    continue
            else:
                result.append(intervals[i])
        if begin == -1 and end == -1:
            result.append(newInterval)
        return result
    def process(self, item, num):
        if num >= item.start and num <= item.end:
            return 0
        if num < item.start:
            return -1
        if num > item.end:
            return 1