class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        path_arr = path.split("/")
        for p in path_arr:
            if p == "" or p == ".":
                continue
            if p == "..":
                if st:
                    st.pop()
            else:
                st.append(p)
        return "/" + "/".join(st)
