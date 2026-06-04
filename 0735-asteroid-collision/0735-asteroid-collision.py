class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if a > 0:
                st.append(a)
                continue
            alive = True           # 标记当前向左星球是否存活
            while st and st[-1] > 0:
                top = st[-1]
                if top > -a:
                    alive = False  # 当前星球被销毁
                    break
                elif top == -a:
                    st.pop()
                    alive = False  # 同归于尽，也不入栈
                    break
                else:
                    st.pop()
            if alive:
                st.append(a)
        return st