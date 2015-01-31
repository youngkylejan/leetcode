class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) <= 0:
            return 0
        stack = []
        ans = 0
        left = -1
        for i in range(0, len(s)):      
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) <= 0:
                    left = i
                else:
                    stack.pop()
                    if len(stack) <= 0:
                        ans = max(ans, i - left)
                    else:
                        ans = max(ans, i - stack[len(stack) - 1])
        return ans