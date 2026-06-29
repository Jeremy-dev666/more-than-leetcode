class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        ans = 0

        for r_bound in range(n + 1):
            cur_h = 0 if r_bound == n else heights[r_bound]
            while st and cur_h < heights[st[-1]]:
                cur_idx = st.pop()
                l_bound = st[-1] if st else -1
                area = (r_bound - l_bound - 1) * heights[cur_idx]
                ans = max(ans, area)
            st.append(r_bound)
        
        return ans