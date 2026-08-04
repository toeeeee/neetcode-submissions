class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        first = (temperatures[0],0)
        st = [first]
        
        for i, t in enumerate(temperatures):
            if i==0:
                continue

            print(t, st[-1][0])
            # guess:
            # add a count to everything beneath the popped item 
            # that currently exists in the stack
            # and the item itself?
            while st and t > st[-1][0]:
                (popped,popped_i) = st.pop()
                print(f"popped ({popped},{popped_i})")
                result[popped_i] += 1
                # other items in stack
                for prev, prev_i in st:
                    result[prev_i] += 1 
            
            st.append((t,i))
            print(f"stack is {st}")

        #non popped items have nothing bigger than them
        for prev, prev_i in st:
            result[prev_i] = 0
        
        return result





            
        