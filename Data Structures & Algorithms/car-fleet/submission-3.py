from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create reversed pos stack
        st = []
        for i, pos in enumerate(position):
            st += [(pos, speed[i])]
        st.sort()


        # Calculate times
        fleets_added = 0
        while len(st)>1:
            last = st.pop()
            last_time = (target-last[0])/last[1]
            top = st.pop()
            current_time = (target-top[0])/top[1]
            if (current_time<=last_time):
                st.append(last)
            else:
                st.append(top)
                fleets_added += 1
        
        return 1 + fleets_added



        
        