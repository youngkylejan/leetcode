class Solution:
	# @param height, a list of integer
	# @return an integer
	def largestRectangleArea(self, height):

		if not height:
			return 0

		area = 0
		stack = []
		stack.append(0)
		height.append(0)

		for i in range(1, len(height)):
			while stack and height[stack[-1]] > height[i]:
				h = height[stack.pop()]
				w = i - stack[-1] - 1 if stack else i
				area = max(area, h * w)
			stack.append(i)

		return area