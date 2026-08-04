class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        cur, max = None, 0

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            
            if count[n] > max:
                cur = n
                max = count[n]

        return cur

            
        