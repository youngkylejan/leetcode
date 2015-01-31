class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = filter(str.isalnum, s)
        s = s.lower()
        while len(s) > 0:
            if s[0] == s[len(s) - 1]:
                s = s[1:len(s)-1]
            else:
                return False
            return True