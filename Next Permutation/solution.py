class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):

        flag = False

        for i in range(len(num) - 1, 0, -1):
            if num[i] > num[i - 1]:
                for j in range(len(num) - 1, i - 1, -1):
                    if num[j] > num[i - 1]:
                        break

                flag = True
                self.swap(num, i - 1, j)

                k = i
                t = len(num) - 1
                while k != t and k - 1 != t:
                    self.swap(num, k, t)
                    k = k + 1
                    t = t - 1
                break

        if flag == False:
            return sorted(num)
        else:
            return num

    def swap(self, a, x, y):
        # print str(x) + " " + str(y)
        a[x] = a[x] ^ a[y]
        a[y] = a[x] ^ a[y]
        a[x] = a[x] ^ a[y]