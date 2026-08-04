class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        p = [nums[0]]
        s = [nums[-1]]
        for i in range(1,n):
            p.append(p[i-1]*nums[i])
            s.append(s[i-1]*nums[-1-i])
        
        res = [s[n-2]]
        if n-2 > 0:
            for j in range(n-2):
                res.append(p[j] * s[n-3-j]) 
        res.append(p[n-2])
        
        return res