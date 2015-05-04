class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        i = 0
        j = 0
        len1 = len(haystack)
        len2 = len(needle)

        next = [0] * len(needle)
        self.getNext(needle, next)

        while i < len1 and j < len2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == len2:
            return i - j
        else:
            return -1

    def getNext(self, p, next):
        
        if len(next) <= 0:
            return

        plen = len(p)
        next[0] = -1

        k = -1
        j = 0

        while j < plen - 1:
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1

                if p[j] != p[k]:
                    next[j] = k
                else:
                    next[j] = next[k]
            else:
                k = next[k]
