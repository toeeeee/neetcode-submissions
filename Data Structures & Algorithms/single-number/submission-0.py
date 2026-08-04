class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = 0
        for num in nums: 
            hashmap[num] += 1
        for num in hashmap:
            if hashmap[num] == 1:
                return num