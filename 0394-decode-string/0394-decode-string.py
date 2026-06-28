class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cur_num = 0
        cur_str = ""

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                st.append((cur_num, cur_str))
                cur_num = 0
                cur_str = ""
            elif c == "]":
                prev_num, prev_str = st.pop()
                cur_str = prev_str + prev_num * cur_str
            else:
                cur_str += c
        return cur_str