class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for x in asteroids:
            # 只有a向右x向左才会碰撞
            # a向左x向右，或者a、x都向右就不会碰撞
            # 先排除 x > 0 的情况：
            if x > 0:
                st.append(x)
                continue

            while st and st[-1] > 0:
                if -x > st[-1]:
                    st.pop()
                elif -x == st[-1]:
                    st.pop()
                    break
                else:
                    break
            
            else:
                st.append(x)

        return st
