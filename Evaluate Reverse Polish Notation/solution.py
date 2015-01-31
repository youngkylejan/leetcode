class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in range(0, len(tokens)):
                        operator = tokens[i]
            if operator.isdigit() or (operator[0] == "-" and operator[1:len(operator)].isdigit()):
                stack.append(int(operator))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                ans = 0
                if operator == "+":
                    ans = num1 + num2
                elif operator == "-":
                    ans = num1 - num2
                elif operator == "*":
                    ans = num1 * num2
                else:
                    ans = abs(num1) / abs(num2)
                    if (num1 > 0) ^ (num2 > 0) is True:
                        ans = -ans
                stack.append(ans)
        return stack.pop()