class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        while tokens:
            top = tokens.pop(0)

            if top:
                try:
                    st.append(int(top))
                except:
                    b = st.pop()
                    a = st.pop()
                    match top:
                        case "+":
                            s = a+b
                        case "-":
                            s = a-b
                        case "*":
                            s = a*b
                        case "/":
                            s = int(a/b)
                    st.append(s)

                # check if last operation
                if not tokens:
                    return st.pop()

                    


                    




        