class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        
        root = nodes[0]
        if root[1] != -1:
            return False

        st = [root[0]]
        for node in nodes[1:]:
            while st and node[1] != st[-1]:
                st.pop()
            if not st:
                return False
            st.append(node[0])

        return True