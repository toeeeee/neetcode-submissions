class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        n = len(s)

        if n==0 or n==1:
            return n
 
        res = 0
        chars = {s[0]}
        while r>l and r < n:
            c = s[r]
            if c not in chars:
                chars.add(c)
            else:
                while c in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(c)
            
            res = max(res, r-l+1)
            r += 1

        return res
        