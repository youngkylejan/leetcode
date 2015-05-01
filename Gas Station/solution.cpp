class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        
        int start = gas.size() - 1;
        int end = 0;
        int used = gas[start] - cost[start];

        while (start > end) {
            if (used <= 0) {
                start -= 1;
                used += gas[start] - cost[start];
            } else {
                used += gas[end] - cost[end];
                end += 1;
            }
        }

        return (used >= 0 ? start : -1);
    }
};