class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        l = []
        for item in num:
            l.append(str(item))
        l = sorted(l, key = str.lower)
        l = sorted(l, cmp = self.compare)
        l.reverse()
        if l[0] == "0":
            return l[0]
        ans = ""
        for item in l:
            ans = ans + item
        return ans
    def compare(self, str2, str1):
        l1 = len(str1)
        l2 = len(str2)
        if str1 != str2[0:len(str1)]:
            return 1
        if int(str2) - int(str1 + str2[0 : l2 - l1]) != 0:
            return int(str2) - int(str1 + str2[0 : l2 - l1])
        else:
            return int(str1) - int(str2[len(str2) - len(str1):len(str2)])