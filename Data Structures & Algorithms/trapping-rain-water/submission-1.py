class Solution:
    def trap(self, height: List[int]) -> int:
        # actual two pointer solution similar to most area inbetween bars
        # idea is that taller pointer doesnt matter- save information for later
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        area = 0

        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])

            if lMax < rMax:
                ith = lMax - height[l]
                l += 1
            else: 
                ith = rMax - height[r]
                r -= 1

            if ith > 0:
                area += ith

        return area 

        