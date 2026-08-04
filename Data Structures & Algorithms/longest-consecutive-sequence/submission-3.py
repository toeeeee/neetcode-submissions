class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        s = set(nums)
        for n in s:
            if n-1 not in nums:
                length = 1
                start = n
                nxt = start+1 
                while nxt in nums:
                    length += 1 
                    nxt += 1

                res = max(res,length)

        return res


