class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += f"{n}#"
            encoded += f"{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        sol = []
        cur = ""

        read = False
        numstr = ""
        for c in s:
            if read:
                if count > 0:
                    cur += f"{c}"
                    count -= 1
                    if count == 0:
                        sol.append(cur)
                        cur = ""
                        numstr = ""
                        read = False
            else:
                if c.isnumeric():
                    numstr += c
                if c=='#':
                    read = True
                    count = int(numstr)
                    if count == 0: #dumb ass edge case but whatever
                        sol.append("")
                        numstr = ""
                        read = False
        
        return sol

        

