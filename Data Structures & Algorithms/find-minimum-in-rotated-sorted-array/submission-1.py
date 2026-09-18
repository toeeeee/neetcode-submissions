class Solution:
    # Need to find start and end of rotations to do proper binary search
    # The main question is how many rotations do we have?
    # If we knew we would just rotate the list back to where it was and search for item
    # So there has to be some sort of trick

    # APPROACHES:
    # difference between ends is always -1 except for original
    # e-s < 0 for all permutations except for 
    # ok all these mathmatical approaches suck

    # Takeaway: Binary search works like a normal search on sorted sections not just a complete sort
    # 


    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        cut = (nums[i], i) # value, index
        while i <= j:
            m = (i+j)//2
            if nums[m] < cut[0]:
                cut = (nums[m], m)
                j = m - 1
            else:
                i = m + 1
        return cut[0]


