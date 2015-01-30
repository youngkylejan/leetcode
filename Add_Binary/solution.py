class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):

		l1 = len(a) - 1
		l2 = len(b) - 1

		ans = ""
		carry = 0

		while l1 >= 0 and l2 >= 0:
			ans = str(int(a[l1]) ^ int(b[l2]) ^ carry) + ans
			carry = 1 if int(a[l1]) + int(b[l2]) + carry >= 2 else 0
			l1 = l1 - 1
			l2 = l2 - 1

		while l1 >= 0:
			ans = str(int(a[l1]) ^ carry) + ans
			carry = 1 if int(a[l1]) + carry >= 2 else 0
			l1 = l1 - 1

		while l2 >= 0:
			ans = str(int(b[l2]) ^ carry) + ans
			carry = 1 if int(b[l2]) + carry >= 2 else 0
			l2 = l2 - 1

		ans = str(carry) + ans if carry >= 1 else ans

		return ans

