class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 1

        for num in nums:
            if num == cur:
                count += 1 
            else:
                count -= 1
                if count < 0:
                    cur = num
                    count += 2 
        if count == 0: 
            return none
        return cur
            
        