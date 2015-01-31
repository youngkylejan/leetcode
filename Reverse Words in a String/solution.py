class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l = s.split(" ")
        str = ""
        for i in range(len(l) - 1, 0, -1):
            if l[i] == '':
                continue
            str = str + l[i] + " "
        str = str + l[0]
        return str.strip()