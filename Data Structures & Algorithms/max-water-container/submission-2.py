class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = -1
        height = -1
        while l<r:
            if heights[l] < heights[r]:
                height = heights[l]
                area = (r-l)*height
                l += 1
            else:
                height = heights[r]
                area = (r-l)*height
                r -= 1
            max_area = max(max_area,area)
        return max_area    
        