class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                st.append(int(c))
            else:
                b = st.pop()
                a = st.pop()
                match c:
                    case "+":
                        st.append(a + b)
                    case "-":
                        st.append(a - b)
                    case "*":
                        st.append(a * b)
                    case "/":
                        st.append(int(a / b))
        
        return st[-1]