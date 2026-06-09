class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for x in asteroids:
            # 向右直接压栈
            if x > 0:
                st.append(x)
                continue
            # 向左的需要和栈顶向右的比较看会不会爆炸
            while st and st[-1] > 0:
                top = st[-1]
                if top <= -x:  # 栈顶小行星爆炸
                    st.pop()
                if top >= -x:  # x 爆炸
                    break
            # while 没有 break，说明 x 没有爆炸，入栈
            else:  
                st.append(x)
        return st