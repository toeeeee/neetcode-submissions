class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # they lied when they said they want distinct indices ... 
        # they only care are unique triplets in the sense of the items not the indices
        res = []

        nums = sorted(nums)
        i = 0 
        n = len(nums)
        l = i+1
        r = n-1
        while i < n:
            if i == n-1:
                break

            if r <= l or l >= r:
                i += 1 
                l = i+1
                r = n-1
                continue

            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                triplet = [nums[i],nums[l],nums[r]]
                if triplet not in res: 
                    res.append(triplet)
                l += 1
        return res

            

        

        