class Solution:
    # @return an integer
    def maxArea(self, height):
        p = 0
        q = len(height) - 1
        area = 0
        while p < q:
            if (q - p) * (height[p] if height[p] < height[q] else height[q]) > area:
                area = (q - p) * (height[p] if height[p] < height[q] else height[q])
            if height[p] < height[q]:
                p = p + 1
            else:
                q = q - 1
        return area