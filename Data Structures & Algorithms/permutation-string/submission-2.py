class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = {} # permutation hash
        for c in s1:
            if c not in chars1:
                chars1[c] = 1
            else:
                chars1[c] += 1
        
        print(chars1)

        n1 = len(s1)
        n2 = len(s2)

        l = 0
        r = 0
        chars2 = {} # window hash
        while l <= r and r < n2:
            c = s2[r]
            if c not in chars2:
                chars2[c] = 1
            else:
                chars2[c] += 1

            #print(f"r: {r}")
            #print(f"{chars2}")

            if chars2==chars1:
                return True

            r += 1
            if r-l+1 > n1: # window stays fixed to size of s1 + hash update
                leftmost = s2[l]
                chars2[leftmost] -= 1
                if chars2[leftmost] <= 0:
                    chars2.pop(leftmost)
                l += 1
        
        return False

        