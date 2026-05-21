class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = min(height[l], height[r]) * (r-l)

        for i in range(len(height)):
            if height[l] < height[r]:
                l += 1
                area =  min(height[l], height[r]) * (r-l)
                max_area = max(max_area, area)
            else:
                r -= 1
                area = min(height[l], height[r]) * (r-l)
                max_area = max(max_area, area)
        
        return max_area