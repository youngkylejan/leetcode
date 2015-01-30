class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):

		if len(num) <= 3:
			return []

		result = []

		for i in range(0, len(num) - 3):
			if i > 0 and num[i] == num[i - 1]:
				continue

			for j in range(len(num) - 1, 0, -1):
				if j < len(num) - 1 and num[j] == num[j + 1]:
					continue

				p = i + 1
				q = j - 1

				cur = num[i] + num[j]
				while p < q:
					tmp = cur + num[p] + num[q]
					if tmp == target:
						result.append([num[i], num[p], num[q], num[j]])
						p = p + 1
						while p < q and num[p] == num[p - 1]: p = p + 1
						q = q - 1
						while p < q and num[q] == num[q + 1]: q = q - 1
					elif tmp < target:
						p = p + 1
					else:
						q = q - 1

		return result
