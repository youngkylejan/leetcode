class Solution {
public:
    int maxArea(vector<int>& height) {

        int area = 0;
        int p = 0, q = height.size() - 1;

        while (p < q) {
            
            if (height[p] < height[q])
                area = max(area, height[p] * (q - p));
            else
                area = max(area, height[q] * (q - p));

            if (height[p] < height[q])
                p++;
            else
                q--;
        }

        return area;      
    }
};