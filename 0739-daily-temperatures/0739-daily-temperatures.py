class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans