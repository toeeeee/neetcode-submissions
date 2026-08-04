class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        first = (temperatures[0],0)
        st = [first]
        
        for i, t in enumerate(temperatures):
            if i==0:
                continue

            while st and t > st[-1][0]:
                popped,popped_i = st.pop()
                result[popped_i] = i-popped_i
            st.append((t,i))
        return result





            
        