class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ""
        cur_num = 0
        st = []

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                st.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif c == "]":
                prev_str, num = st.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += c

        return cur_str