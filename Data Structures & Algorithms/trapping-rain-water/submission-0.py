class Solution:
    def trap(self, height: List[int]) -> int:
        # find greatest values to left and right of 0, minimum of both
        # subtract by amount of ground

        n = len(height)
        
        l = [0 for i in range(n)] 
        m = -1
        for i in range(1,n-1):
            m = max(m, height[i-1])
            l[i]=m

        r = [0 for i in range(n)] 
        m = -1
        for j in range(n-2,0,-1):
            m = max(m, height[j+1])
            r[j] = m

        area = 0
        for k in range(n):
            ith = min(l[k],r[k])-height[k]
            if ith > 0:
                area += ith
        
        return area
