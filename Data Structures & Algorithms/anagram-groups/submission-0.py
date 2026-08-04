class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            char_freq = [0 for i in range(26)]
            for char in s:
                num = ord(char) - 97
                char_freq[num] += 1
            char_freq = tuple(char_freq)
            
            if char_freq in h:
                h[char_freq] += [s]
            else:
                h[char_freq] = [s]
        
        return list(h.values())

        
