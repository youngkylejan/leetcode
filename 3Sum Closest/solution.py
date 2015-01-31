class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):

		num = sorted(num)

		ans = 0
		mindis = 999999

		for i in range(0, len(num)):
			if i > 0 and num[i] == num[i - 1]:
				continue

			p = i + 1
			q = len(num) - 1

			while p < q:
				cur = num[i] + num[p] + num[q]
				theta = target - cur

				if abs(theta) < mindis:
					mindis = abs(theta)
					ans = cur
				elif cur < target:
					p = p + 1
				else:
					q = q - 1

		return ans
