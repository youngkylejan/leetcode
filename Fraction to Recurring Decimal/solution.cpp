class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {

        if (numerator == 0)
            return "0";

        string res = (numerator >= 0) ^ (denominator >= 0) == false ? "" : "-";

        long a = abs((long)numerator);
        long b = abs((long)denominator);

        stringstream ss;
        ss << a / b;
        res += ss.str();

        if (a % b == 0)
            return res;

        res += ".";

        unordered_map<int, int> pos_map;
        
        long x = a % b;
        string frac = "";

        while (x) {
            long d = (x * 10) / b;
            ss.str("");
            ss << d;
            frac += ss.str();

            pos_map[x] = frac.size() - 1;

            x = (x * 10) % b;

            if (pos_map.find(x) != pos_map.end()) {
                int i = pos_map[x];
                res += string(frac, 0, i) + "(" + string(frac, i, frac.size() - i) + ")";
                return res;
            }
        }

        return res + frac;
    }
};