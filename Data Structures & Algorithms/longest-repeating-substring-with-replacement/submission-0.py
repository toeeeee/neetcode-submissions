class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        chars = {}
        l = 0
        r = 0
        res = -1
        while l <= r and r < n:
            c = s[r]
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1

            #print(f"r: {r}, chars after update {chars}")

            # want to keep greatest amt of characters to reduce replacements      
            num_replacements = (r-l+1) - max(chars.values())
            print(num_replacements)
            if num_replacements > k:
                #print('opt a')
                chars[s[l]] -= 1
                l += 1 
            else:
                #print('optb')
                #print(f"{res},{r-l+1}")
                res = max(res, r-l+1)

            r += 1

        return res
        