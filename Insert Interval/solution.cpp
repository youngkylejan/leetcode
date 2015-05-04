/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {

        int first = 0;
        vector<Interval> ans;

        while (first < intervals.size() && newInterval.start > intervals[first].end) {
            ans.push_back(intervals[first]);
            first++;
        }

        int start = newInterval.start;
        int end = newInterval.end;

        while (first < intervals.size() && end >= intervals[first].start) {
            start = min(start, intervals[first].start);
            end = max(end, intervals[first].end);
            first++;
        }

        intervals.insert(intervals.begin() + first, Interval(start, end));

        while (first < intervals.size())
            ans.push_back(intervals[first++]);

        return ans;
    }
};