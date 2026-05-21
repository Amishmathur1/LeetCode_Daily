def findArea(l, r, height):
        return min(height[l], height[r]) * (r-l)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = min(height[l], height[r]) * (r-l)

        for i in range(len(height)):
            if height[l] < height[r]:
                l += 1
                max_area = max(max_area, findArea(l,r,height))
            else:
                r -= 1
                max_area = max(max_area, findArea(l,r,height))
        
        return max_area