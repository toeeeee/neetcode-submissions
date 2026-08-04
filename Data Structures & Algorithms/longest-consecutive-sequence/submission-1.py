class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0

        for n in nums:
            if n-1 not in nums:
                length = 1
                start = n
                nxt = start+1 
                while nxt in nums:
                    length += 1 
                    nxt += 1

                if length > res:
                    res = length

        return res


