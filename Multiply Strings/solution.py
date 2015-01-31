class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) > len(num2):
            tmp = num1[0:len(num1)]
            num1 = num2[0:len(num2)]
            num2 = tmp[0:len(tmp)]
            del tmp
        plus = []
        for i in range(0, len(num1)):
            first = int(num1[i])
            carry = 0
            plusNum = ""
            for j in range(0, len(num2) + 1):
                second = int(num2[j]) if j < len(num2) else 0
                product = first * second + carry
                plusNum = plusNum + str(product % 10) if product != 0 or j < len(num2) else plusNum
                carry = product / 10
            plus.append(plusNum)
        if len(plus) <= 1:
            return plus[0][::-1]
        for i in range(0, len(plus)):
            plus[i] = "0" * i + plus[i]
        result = plus[0]
        for k in range(1, len(plus)):
            plusNum = ""
            i = 0
            carry = 0
            for i in range(0, len(plus[k]) + 1):
                first = int(result[i]) if i < len(result) else 0
                second = int(plus[k][i]) if i < len(plus[k]) else 0
                tmp = first + second + carry
                plusNum = plusNum + str(tmp % 10) if tmp != 0  or i < len(plus[k]) else plusNum
                carry = tmp / 10
            result = plusNum
        return result[::-1]