class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        tail = len(A) - 1
        head = 0
        for i in range(0, tail + 1):
            while A[i] == 2 and i < tail:
                self.swap(A, i, tail)
                tail = tail - 1
            while A[i] == 0 and i > head:
                self.swap(A, i , head)
                head = head + 1
    def swap(self, A, a, b):
        A[a] = A[a] ^ A[b]
        A[b] = A[a] ^ A[b]
        A[a] = A[a] ^ A[b]