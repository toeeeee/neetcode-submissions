class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(i,j,target):
            while i <= j:
                m = (i+j)//2
                val = nums[m]
                if val == target:
                    return m
                elif val > target:
                    j = m - 1
                else: 
                    i = m + 1
            return -1

        n = len(nums)-1
        i, j = 0, n
        cut = (nums[i], i) # value, index
        while i <= j:
            m = (i+j)//2
            if nums[m] < cut[0]:
                cut = (nums[m], m)
                j = m - 1
            else:
                i = m + 1

        a = binarySearch(0,cut[1],target)
        b = binarySearch(cut[1],n,target)
        return a if a>-1 else b
        