class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        n = len(heights)

        for r in range(n + 1):
            cur_h = 0 if r == n else heights[r]
            # 当 cur_h < heights[st[0]] 时说明找到了栈顶元素的右边界
            while st and cur_h < heights[st[-1]]:
                # 由于维持的栈是单调递增的
                # 所以弹出当前栈顶元素后的栈顶元素就是左边界
                idx = st.pop()
                l = -1 if not st else st[-1]
                area = (r - l - 1) * heights[idx]
                ans = max(ans, area)
            
            st.append(r)

        return ans

            