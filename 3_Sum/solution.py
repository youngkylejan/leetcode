class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):

		num = sorted(num)

		result = []
		
		for i in range(0, len(num)):
			if i > 0 and num[i] == num[i - 1]:
				continue

			p = i + 1
			q = len(num) - 1

			while p < q:
				target = num[i] + num[p] + num[q]

				if target == 0:
					result.append([num[i], num[p], num[q]])
					p = p + 1
					while p < q and num[p] == num[p - 1]: p = p + 1
					q = q - 1
					while p < q and num[q] == num[q + 1]: q = q - 1
					
				elif target < 0:
					p = p + 1
				else:
					q = q - 1

		return result
