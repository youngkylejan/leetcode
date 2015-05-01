class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        
        hashs = {}

        for i in range(1, 27):
            hashs[i] = chr(ord('A') + i - 1)

        str = ""
        while n > 0:
            remain = n % 26
            c = hashs[remain] if remain != 0 else 'Z'
            n = n / 26

            if remain == 0:
                n -= 1

            str = c + str

        return str