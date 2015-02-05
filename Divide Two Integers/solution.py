class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if abs(dividend) < abs(divisor):
            return 0
        flag = 1 if (dividend > 0) ^ (divisor > 0) is False else -1
        
        a = abs(dividend)
        d = abs(divisor)
        ans = 0
        while a >= d:
            b = d
            ex = 1
            while b << 1 < a:
                b = b << 1
                ex = ex << 1
            
            ans = ans + ex
            a = a - b
        
        ans = ans if flag == 1 else -ans
        if ans > 2147483647:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        
        return ans 
        