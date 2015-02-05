class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator / denominator)
        sign = 1 if (numerator > 0) ^ (denominator > 0) is False else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        maps = {}
        tmp = str(numerator / denominator) + "." if numerator / denominator != 0 else "0."
        remainer = 0
        ans = ""
        while True:
            remainer = numerator % denominator
            if remainer in maps.keys():
                ans = ans + tmp[0:maps[remainer]] + "(" + tmp[maps[remainer]:len(tmp)] + ")"
                break
            maps[remainer] = len(tmp)
            numerator = remainer * 10
            tmp = tmp + str(numerator / denominator)
            if numerator <= 0:
                ans = ans + tmp[0:len(tmp)-1]
                break
        return ans if sign == 1 else "-" + ans