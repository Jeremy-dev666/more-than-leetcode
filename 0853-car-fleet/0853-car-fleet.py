class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        time = [0] * n
        for i, (pos, sp) in enumerate(sorted(zip(position, speed))):
            time[i] = (target - pos) / sp
        st = []
        for t in time:
            while st and st[-1] <= t:
                st.pop()
            st.append(t)

        return len(st)